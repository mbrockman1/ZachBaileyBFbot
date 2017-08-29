
# coding: utf-8

# In[3]:


import tweepy
import json
from random import randint
import pickle
from constants import *


# In[4]:


#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object

list_of_helpfuls = ['Great Tweet!', 'Love it!',
                    'Oh man, you are killing it!', 'Nice!',
                    'No way!', 'I love you Zach',
                    'This, is gold!', 'Hahaha my sides!',
                    'Fuck you!', 'Man you are looking pretty strong!',
                    'Way to go!', 'This was a good tweet, I am so proud',
                    'Drinking again, haha just kidding.']


# In[8]:




# This is the listener, resposible for receiving data

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        user = 'freshzb'
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        fav_status = api.user_timeline(user)[0].__dict__['favorited']
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        if fav_status == False:
            try:
                api.update_status(status='@freshZB  %s' % list_of_helpfuls[randint(0, len(list_of_helpfuls) - 1)],
                                  in_reply_to_status_id=str(api.user_timeline(user)[0].__dict__['id']))
                api.create_favorite(api.user_timeline(user)[0].__dict__['id'])
            except:
                pass
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    while True:
        try:
            l = StdOutListener()
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_secret)

            print('Running...')
            # There are different kinds of streams: public stream, user stream, multi-user streams
            # For more details refer to https://dev.twitter.com/docs/streaming-apis
            stream = tweepy.Stream(auth, l)
            stream.filter(follow=['627933139'])
        except(Exception, e):
            print("Error. Restarting Stream.... Error: ")
            print(e.__doc__)
            print(e.message)


# In[ ]:




