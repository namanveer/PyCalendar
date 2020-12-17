#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


# In[24]:


from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
   
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Getting the upcoming 15 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=15, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print(start+' - '+ end, event['summary']+'-'+event['description'])


if __name__ == '__main__':
    main()


# In[ ]:




