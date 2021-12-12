import tweepy
from datetime import datetime

# {{ AUTH }}
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth, wait_on_rate_limit = True)
# {{ END AUTH }}

# {{ CODING }}
def Tweet(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

x =  datetime.today().strftime('%A')
Tweet(" ",x+".jpg")
# {{ END CODING }}
