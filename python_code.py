__author__ = 'chan'

from flask import Flask, render_template, request
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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html_page.html')

@app.route('/result', methods=['POST'])
def result():
    keyword = request.form['keyword']
    location = request.form['location']
    auth = tweepy.OAuth1UserHandler(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
	)
    tweets = api.search_tweets(keyword, tweet_mode="extended")

    for tweet in tweets:
        try:
            return(tweet.retweeted_status.full_text)
            return("=====")
        except AttributeError:
            return(tweet.full_text)
            return("=====")
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
