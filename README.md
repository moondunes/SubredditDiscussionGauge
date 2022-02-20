# Subreddit Discussion Gauge
A simple python project that grabs and counts words from subreddit posts to see what topics are being discussed most often.

The goal of this python script is to filter posts from a subreddit based on criteria you choose and count how many times a word is mentioned in those posts. It includes filters for stopwords (e.g. pronouns, conjunctions, etc.) alongside a filter you can set yourself. For example, if you are trying to get data on r/nfl, you may want to ignore the word "football" as a keyword. You can also add the oddball punctuation that comes through and messes up your tokenizer, as the tokenizer does not play well with punctuation.

Things you need to set yourself:
- Reddit login access
- Subreddit(s)
- Custom stopwords
- Search criteria

## Config.py Setup
https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/ 
This is a helpful guide for getting information on setting up a bot to get your Client_ID and Client_Agent. NOTE: You typically want to create a separate account specifically to use as a bot instead of your own username and password.

## Resources.py Setup
You will want to add words to the ADDITIONAL_STOPWORDS array that you don't care about keeping track of. The default NLTK_STOPWORDS is a good start, but not all-encompassing. I included some extra words already that I found unnecessary, but you can add or remove as you please. You can also add oddball punctuation marks you find, as sometimes punctuation comes through in different formats and can screw up your tokenizer. I added the curly quotes to the python's default string.punctuation(), and you can add or remove more as you see fit.

## Main.py setup
https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.search
I highly suggest getting yourself familiar with this PRAW documentation, as it will define how you grab your posts. By default, PRAW only grabs 25 posts, so you may want to set limit=None, which hits the cap of 1000 for PRAW. I left a few defaults to comment in/out.

## Results.txt
Just a plain text file to write your results to, nothing fancy here!
