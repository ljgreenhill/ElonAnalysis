#referenced this https://gist.github.com/yanofsky/5436496

import tweepy
import csv

auth = tweepy.OAuthHandler(CONSUMER, CONSUMER_SECRET)
auth.set_access_token(ACCESS, ACCESS_SECRET)
api = tweepy.API(auth)

alltweets = []
new_tweets = api.user_timeline(screen_name = 'elonmusk',count=200)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1

while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name = 'elonmusk',count=200,max_id=oldest)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

csvRows = []
for tweet in alltweets:
    csvRows.append([tweet.id, tweet.favorite_count, tweet.retweet_count, tweet.created_at, tweet.text])
    print("ID: " + str(tweet.id) + ", Favorites: " + str(tweet.favorite_count) + ", Retweets: " + str(tweet.retweet_count) + ", Time Created: " + str(tweet.created_at) + ", Text: " + str(tweet.text)) 

with open('tweets.csv', 'w', newline='', encoding = "utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', "Favorites", "Retweets", "Date Created", "Text"])
    for row in csvRows:
        writer.writerow(row)
