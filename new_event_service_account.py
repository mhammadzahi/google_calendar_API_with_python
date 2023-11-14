from google.oauth2 import service_account
import googleapiclient.discovery


credentials = service_account.Credentials.from_service_account_file('creds_service_account.json', scopes=['https://www.googleapis.com/auth/calendar'])
service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)


event = {
    'summary': 'Sample Event2',
    'location': 'Sample Location',
    'description': 'This is a sample event created using Python.',
    'start': {
        'dateTime': '2023-10-14T10:00:00',  # Replace with the start date and time of your event
        'timeZone': 'Asia/Dubai'
    },
    'end': {
        'dateTime': '2023-10-14T12:00:00',  # Replace with the end date and time of your event
        'timeZone': 'Asia/Dubai'
    },
}

created_event = service.events().insert(calendarId='38d41dff8e9e638b468d359e1ceafe682641849352bcf879dd59cdc465cd9a5b@group.calendar.google.com', body=event).execute()


print(f'Event created: {created_event.get("htmlLink")}')
