import time
import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("API_KEY")
API_SECRET=os.getenv("API_SECRET")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
ACCESS_SECRET=os.getenv("ACCESS_SECRET")

auth=tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api = tweepy.API(auth)

# user=api.get_user('kisadivoire')
# print(user.screen_name)
# print(user.followers_count)

# api.update_status(status='Hello, world! (once more)')


# api.update_status_with_media('', '/Users/uliakoverzneva/twitter-bot/img/doggo2.jpg')


# tweets = [
#     ['', '/Users/uliakoverzneva/twitter-bot/img/doggo1.jpg'],
#     ['', '/Users/uliakoverzneva/twitter-bot/img/doggo2.jpg']
# ]

# for tweet in tweets:
#     status = api.update_status_with_media( tweet[0], tweet[1])
#     time.sleep(86400)

new_tweet = "This tweet comes from tweepy"
api.update_status(new_tweet)
