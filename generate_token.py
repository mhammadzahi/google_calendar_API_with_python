import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def authenticate():
    creds = None
    token_file = 'token_miramar.json'
    credentials_file = 'calendar-api.json'
    scopes = ['https://www.googleapis.com/auth/calendar']

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
            creds = flow.run_local_server(port=0)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    
    return creds


def create_event():
    creds = authenticate()

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': 'test!',
        'location': 'Abu Dhabi Al Wahda',
        'start': {
            'dateTime': '2023-10-15T10:00:00',
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': '2023-10-15T11:00:00',
            'timeZone': 'America/New_York',
        },
    }

    calendar_id = 'primary'
    event = service.events().insert(calendarId=calendar_id, body=event).execute()

    print('Event created: %s' % (event.get('htmlLink')))


create_event()

