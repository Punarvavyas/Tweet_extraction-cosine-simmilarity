import csv, re, pandas as pd
import re
from collections import Counter


# Taken from: https://github.com/s/preprocessor/blob/master/preprocessor/defines.py

class Patterns:
    URL_PATTERN = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
    HASHTAG_PATTERN = re.compile(r'#\w*')
    MENTION_PATTERN = re.compile(r'@\w*')
    RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')

    try:
        # UCS-4
        EMOJIS_PATTERN = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        EMOJIS_PATTERN = re.compile(
            u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

    SMILEYS_PATTERN = re.compile(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", re.IGNORECASE)
    NUMBERS_PATTERN = re.compile(r"(^|\s)(\-?\d+(?:\.\d)*|\d+)")


tweets_df = pd.read_csv('tweets.csv',encoding='utf8')

hashtag = []
stri = ""
ls = []
top = ""
for index, row in tweets_df.iterrows():

    #print(index,row['screen_name'],row['text'])
    if row['screen_name'] == "Google":
        x = re.findall(Patterns.HASHTAG_PATTERN, row['text'].encode().decode())
        if len(re.findall(Patterns.HASHTAG_PATTERN, row['text'])) != 0:
            for i in range(len(x)):
                hashtag.append(x[i])
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", row['text'])

        cle = re.sub(Patterns.MENTION_PATTERN, "", cle.lower())
        cle = re.sub(Patterns.URL_PATTERN, "", cle)
        cle = re.sub(Patterns.HASHTAG_PATTERN, "", cle)
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", cle)
        cle = re.sub(Patterns.SMILEYS_PATTERN, "", cle)
        cle = re.sub(Patterns.NUMBERS_PATTERN, "", cle)
        cle = re.sub(Patterns.EMOJIS_PATTERN, "", cle)
        # print(cle)
        stri = stri + cle
        ls.append(cle)
print("Google:")
print("Hashtags:", hashtag)
# print(stri)
splitlist = stri.split()
Countervar = Counter(splitlist)
most_occur = Countervar.most_common(10)

for i in range(0, 10):
    top = top + most_occur[i][0] + " "
print("Top 10 words:", top)

print("Clean tweets")
for i in range(len(ls)):
    print(i, ls[i])
hashtag = []
stri = ""
ls = []

##################################################################
print("\n\n")
hashtag = []
stri = ""
ls = []
top = ""

for index, row in tweets_df.iterrows():

    # print(index,row['screen_name'],row['text'])
    if row['screen_name'] == "msdev":
        x = re.findall(Patterns.HASHTAG_PATTERN, row['text'])
        if len(re.findall(Patterns.HASHTAG_PATTERN, row['text'])) != 0:
            for i in range(len(x)):
                hashtag.append(x[i])
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", row['text'])
        cle = re.sub(Patterns.MENTION_PATTERN, "", cle.lower())
        cle = re.sub(Patterns.URL_PATTERN, "", cle)
        cle = re.sub(Patterns.HASHTAG_PATTERN, "", cle)
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", cle)
        cle = re.sub(Patterns.SMILEYS_PATTERN, "", cle)
        cle = re.sub(Patterns.NUMBERS_PATTERN, "", cle)
        cle = re.sub(Patterns.EMOJIS_PATTERN, "", cle)
        # print(cle)
        stri = stri + cle
        ls.append(cle)
print("msdev:")
print("Hashtags:", hashtag)
# print(stri)
splitlist1 = stri.split()
Counter0 = Counter(splitlist1)
most_occur = Counter0.most_common(10)

for i in range(0, 10):
    top = top + most_occur[i][0] + " "
print("Top 10 words:", top)

print("Clean tweets")
for i in range(len(ls)):
    print(i, ls[i])
hashtag = []
stri = ""
ls = []

#################################################################
print("\n\n")
hashtag = []
stri = ""
ls = []
top = ""

for index, row in tweets_df.iterrows():

    #print(index,row['screen_name'],row['text'])
    if row['screen_name'] == "RosieBarton":
        x = re.findall(Patterns.HASHTAG_PATTERN, row['text'])
        if len(re.findall(Patterns.HASHTAG_PATTERN, row['text'])) != 0:
            for i in range(len(x)):
                hashtag.append(x[i])
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", row['text'])
        cle = re.sub(Patterns.MENTION_PATTERN, "", cle.lower())
        cle = re.sub(Patterns.URL_PATTERN, "", cle)
        cle = re.sub(Patterns.HASHTAG_PATTERN, "", cle)
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", cle)
        cle = re.sub(Patterns.SMILEYS_PATTERN, "", cle)
        cle = re.sub(Patterns.NUMBERS_PATTERN, "", cle)
        cle = re.sub(Patterns.EMOJIS_PATTERN, "", cle)
        # print(cle)
        stri = stri + cle
        ls.append(cle)
print("RosieBarton:")
print("Hashtags:", hashtag)
# print(stri)
splitlist1 = stri.split()
Counter2 = Counter(splitlist1)
most_occur = Counter2.most_common(10)

for i in range(0, 10):
    top = top + most_occur[i][0] + " "
print("Top 10 words:", top)

print("Clean tweets")
for i in range(len(ls)):
    print(i, ls[i])
hashtag = []
stri = ""
ls = []
#################################################################
print("\n\n")
hashtag = []
stri = ""
ls = []
top = ""

for index, row in tweets_df.iterrows():
    #print("hello",type(row['text']))
    # print(index,row['screen_name'],row['text'])
    if row['screen_name'] == "realDonaldTrump":
        x = re.findall(Patterns.HASHTAG_PATTERN, row['text'])
        if len(re.findall(Patterns.HASHTAG_PATTERN, row['text'])) != 0:
            for i in range(len(x)):
                hashtag.append(x[i])
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", (row['text']))
        cle = re.sub(Patterns.MENTION_PATTERN, "", cle.lower())
        cle = re.sub(Patterns.URL_PATTERN, "", cle)
        cle = re.sub(Patterns.HASHTAG_PATTERN, "", cle)
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", cle)
        cle = re.sub(Patterns.SMILEYS_PATTERN, "", cle)
        cle = re.sub(Patterns.NUMBERS_PATTERN, "", cle)
        cle = re.sub(Patterns.EMOJIS_PATTERN, "", cle)
        #print("hi",cle)
        stri = stri + cle
        ls.append(cle)
print("realDonalTrump:")
print("Hashtags:", hashtag)
# print(stri)
splitlist1 = stri.split()
Counter3 = Counter(splitlist1)
most_occur = Counter3.most_common(10)

for i in range(0, 10):
    top = top + most_occur[i][0] + " "
print("Top 10 words:", top)

print("Clean tweets")
for i in range(len(ls)):
    print(i, ls[i])
hashtag = []
stri = ""
ls = []


