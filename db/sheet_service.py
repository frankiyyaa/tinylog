import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_sheets():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scopes
    )
    client = gspread.authorize(creds)
    return client

def open_sheet():
    client = connect_to_sheets()
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    spreadsheet = client.open_by_key(spreadsheet_id)
    return spreadsheet

def add_user(telegram_id, username, first_name, registered_at):
    spreadsheet = open_sheet()
    users_sheet = spreadsheet.worksheet("Users")

    users_sheet.append_row([
        telegram_id,
        username,
        first_name,
        registered_at
    ])
def get_user(telegram_id):
    spreadsheet = open_sheet()
    users_sheet = spreadsheet.worksheet("Users")
    
    cell = users_sheet.find(telegram_id)
    if cell:
        return users_sheet.row_values(cell.row)
    return None
def update_last_message_id(telegram_id, message_id):
    spreadsheet = open_sheet()
    users_sheet = spreadsheet.worksheet("Users")

    cell = users_sheet.find(telegram_id)
    if cell:
        users_sheet.uodate_cell(cell.row, 5, new_message_id)
