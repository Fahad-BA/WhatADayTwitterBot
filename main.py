import tweepy
from datetime import datetime

# {{ AUTH }}
auth = tweepy.OAuthHandler('K58B9MpBd9e4qSlWczznFDLrc', '2ei2CiuNDvTVgKHlSeDp0PcNFEUwtaGKCCCAvCweVZLcpI2te2')
auth.set_access_token('1070333904970809346-aZdzqDM4Yz26CkNB03eD5Ih53kT9wf', 'LcivNMwMaFP79GBGOf1cW5d9327IzG1xcxlPYHBaqkK7a')
api = tweepy.API(auth, wait_on_rate_limit = True)
# {{ END AUTH }}

# {{ CODING }}
def Tweet(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

x =  datetime.today().strftime('%A')
Tweet(" ",x+".jpg")
# {{ END CODING }}