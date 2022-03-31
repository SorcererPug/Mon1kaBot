# -- IMPORT SECTION --
import praw
import pdb
import re
import os
import random

import variables

# -- CONSTANTS --
REDDIT_USERNAME = "Mon1kaBot"
REDDIT_PASS = "GandalfBot1sStillmyHer0"

# -- INITIALIZE BOT --
reddit = praw.Reddit('bot1')

reddit.login(REDDIT_USERNAME, REDDIT_PASS)

subreddit = reddit.subreddit('sorcererpug')

# -- SEARCH VARIABLES --
keywords = {'Monika', 'MonikaBot', 'Mon1ka', 'Mon1kaBot'} # List of keywords bot looks for

# -- ADD COMMENTS TO ANYONE WHO MENTIONS SEARCH VARIABLES
for comment in subreddit.stream.comments():
    print(comment.body)
    for x in keywords:
        if re.search(x, comment.body, re.IGNORECASE):
           monika_reply = random.choice(variables.bot_phrase_list)
    comment.reply(monika_reply)
    print(monika_reply)

# -- CHANGE FLAIRS --
new_flairs = {'I love you', 'Okay, everyone!', 'Just Monika', "This is so cool, [player]!"}
for submission in subreddit.stream.submissions():
    
    #if random.randint(1,3) == 1:
    new_flair = random.choice(new_flairs)
    new_flair.replace("[player]", submission.author.name)

    submission.mod.flair(text=new_flair))