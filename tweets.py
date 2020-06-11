# -*- coding: utf-8 -*-
import GetOldTweets3 as got
import time
import json
searches=["@PMOIndia", "@RahulGandhi", "@ArvindKejriwal", "#कमीने", '#कुत्ते', '#नीच']
results = []

for query in searches:
    tweetCriteria = got.manager.TweetCriteria().setLang("hi").setQuerySearch(query).setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets:
        results.append(vars(tweet))
    time.sleep(2)
    print(query)

with open('out.txt', 'w+') as fout:
    fout.write('\n'.join(str(results).split('{')))