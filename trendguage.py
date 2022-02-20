import praw
import config
import resources
from collections import OrderedDict
from nltk.tokenize import word_tokenize


def login():
    try:
        reddit = praw.Reddit(
            user_agent=config.user_agent,
            client_id=config.client_id,
            client_secret=config.client_secret,
            username=config.username,
            password=config.password
        )
        print(reddit.user.me())
    except:
        print('Login failed')
    return reddit


def main():
    print('Started')
    reddit = login()
    subreddit = reddit.subreddit(config.subreddit_name)
    posts = subreddit.new()
    #posts = subreddit.hot()
    #posts = subreddit.top()
    #posts = subreddit.search('flair:"<searchFlair>"')
    #posts = subreddit.search('keyword')
    wordcount_dic = {}
    count = 0
    for post in posts:
        count += 1
        title = resources.normalize_string(post.title)
        tokenized_title = word_tokenize(title)
        title_tokens_no_sw = resources.strip_stopwords(tokenized_title)
        for token in title_tokens_no_sw:
            if token in wordcount_dic:
                wordcount_dic[token] += 1
            else:
                wordcount_dic[token] = 1
        if not post.selftext:
            continue
        body = resources.normalize_string(post.selftext)
        tokenized_body = word_tokenize(body)
        body_tokens_no_sw = resources.strip_stopwords(tokenized_body)
        for token in body_tokens_no_sw:
            if token in wordcount_dic:
                wordcount_dic[token] += 1
            else:
                wordcount_dic[token] = 1
    sorted_words = OrderedDict(sorted(wordcount_dic.items(), key=lambda kv: kv[1], reverse=True))
    result_file = open('results.txt','w')
    result_file.write('There were ' +  str(count) + ' posts grabbed from ' + config.subreddit_name + ' with the following non-filtered words found: \n \n')
    for key, val in sorted_words.items():
        result_file.write('"' + key + '" appears ' + str(val) + ' times. \n')
    result_file.close()
    print("Finished")


main()
