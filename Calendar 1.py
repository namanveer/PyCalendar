#!/usr/bin/env python
# coding: utf-8

# In[3]:


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


# In[4]:


pip install google-api python-client


# In[5]:


scopes = ['https://www.googleapis.com/auth/calendar']


# In[9]:


flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()


# In[11]:


service = build('calendar', 'v3', credentials=credentials)


# In[12]:


result = service.calendarList().list().execute()


# In[13]:


calendar_id = result['items'][0]['id']


# In[14]:


result = service.events().list(calendarId=calendar_id).execute()
print(result['items'][0])


# In[15]:


result


# In[21]:


result = service.events().list(calendarId=calendar_id).execute()
print(result['items'][0])


# In[ ]:




