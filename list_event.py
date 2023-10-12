import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def list_events(calendar_id, date):

    credentials = Credentials.from_authorized_user_file('token101.json')


    service = build('calendar', 'v3', credentials=credentials)

    try:
        filtered_events = []
        events_lst = []
        events_result = service.events().list(calendarId=calendar_id, singleEvents=True).execute()
        events = events_result.get('items', [])

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_date = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").date()

            if event_date == date:
                filtered_events.append(event)


        if not filtered_events:
            return 0
            #print('No events found for', date.strftime('%Y-%m-%d'))
        

        else:
            for event in filtered_events: #print('Events for', date.strftime('%Y-%m-%d'))
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))

                events_lst.append({
                'summary': event['summary'],
                'start':start[11:16],
                'end':end[11:16]
                })

        return events_lst

    except Exception as e:
        return 7


#usage
target_date = datetime.date(2023, 6, 2)
calendar_id = 'primary'
print(list_events(calendar_id, target_date))
