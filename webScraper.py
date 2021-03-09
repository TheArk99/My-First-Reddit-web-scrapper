#!/usr/bin/python

import praw
import pandas as pd
import datetime as dt


reddit = praw.Reddit(client_id='8WszHdYn1ggomg',client_secret='J42pyuqiy4FV2Gd79FMcTfPp01NmqQ',user_agent='scrapper',username='The__Ark',password='199Puppies')


subreddit = reddit.subreddit('unixporn')

top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], "comms_num": [], \
                "created": [], \
                "body":[]}


for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)


def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('RedditData.csv', index=False) 

