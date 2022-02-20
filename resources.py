import string
import numpy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

NLTK_STOPWORDS = stopwords.words('english')
ADDITIONAL_STOPWORDS = ['think', 'know', 'would', 'like', 
                        'also', 'could', 'should', 'much', 
                        'actually', 'probably', 'maybe', 'even',
                        'well', 'still', 'already', 'much']
EXPANDED_PUNCTUATION = string.punctuation + '’' + '”' + '“'

def get_stopwords_with_no_punctuation():
    no_punctuation_stopwords = []
    for stopword in NLTK_STOPWORDS:
        if any(char in word_tokenize(EXPANDED_PUNCTUATION) for char in stopword):
            no_punctuation_stopwords.append(normalize_string(stopword))
    return no_punctuation_stopwords

def normalize_string(string_to_normalize):
    return string_to_normalize.upper().translate(str.maketrans('','',EXPANDED_PUNCTUATION))

def strip_stopwords(tokenized_string):
    tokenized_string_no_stopwords = []
    for token in tokenized_string:
        if token in (normalize_string(stopword) for stopword in SUBREDDIT_STOPWORDS) or token.isnumeric():
            continue
        else:
            tokenized_string_no_stopwords.append(token)
    return tokenized_string_no_stopwords

SUBREDDIT_STOPWORDS = numpy.concatenate((
    NLTK_STOPWORDS,
    ADDITIONAL_STOPWORDS,
    word_tokenize(EXPANDED_PUNCTUATION),
    get_stopwords_with_no_punctuation()
    ))


