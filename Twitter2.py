import os
import tweepy
from dotenv import load_dotenv
	
consumer_key = 'LskCm7mALRDFGon10dqFV6dpO'
consumer_secret = '4aPYIqwTn0KMLQLmW5n1R7VFftSa3H0TV2kzvtG2dfwLyq1Hri'
access_token = '1380831414082437120-rCHHrnYHkm6MLAwcPsJdUlmbMUGiPX'
access_token_secret = 'yWV3aavdPVhT9ViqtKdSkrJaNKmBDVTZGhB2IQwrsWuAe'

auth = tweepy.OAuth1UserHandler(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
	)
	
api = tweepy.API(auth)

keyword=input("Enter keyword to search")
location=input("enter location")

tweets = api.search_tweets(keyword, tweet_mode="extended")

for tweet in tweets:
    try:
        print(tweet.retweeted_status.full_text)
        print("=====")
    except AttributeError:
        print(tweet.full_text)
        print("=====")