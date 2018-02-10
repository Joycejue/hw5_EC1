from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk 
## SI 206 - HW
## COMMENT WITH:
## Your section day/time:
## Any names of people you worked with on this assignment:

#usage should be python3 hw5_twitter.py <username_1> <username_2> <num_tweets>
username_1 = sys.argv[1]
username_2 = sys.argv[2]
num_tweets = sys.argv[3]





consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)
#Code for OAuth ends




def make_request_using_cache(baseurl, params):
    
    resp = requests.get(baseurl, params, auth = auth)
    data = json.loads(resp.text)
   
    return data



baseurl = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

params_1 = {}
params_1["screen_name"] = username_1
params_1["count"] = num_tweets
params_2 = {}
params_2["screen_name"] = username_2
params_2["count"] = num_tweets



# Extra Credit 1 (2 pts) Twitter Boggle: Take two twitter accounts and analyze their tweets to find words they have in common and words that are unique to each account. Show the 5 most frequent different (unique) words for each account and the 5 most frequent common words (shared by both).




data_1 = make_request_using_cache(baseurl,params_1)
data_2 = make_request_using_cache(baseurl,params_2)



# data = [{"text":"", }, {}, {}...]


tweets_text_lis_1 = []
for dic in data_1:
	if "text" in dic.keys():
	    tweets_text_lis_1.append(dic["text"]) 
	else:
	    tweets_text_lis_1.append("")	    


text_token_1 = []

for sentence in tweets_text_lis_1:
	text_token_1.append(nltk.word_tokenize(sentence))

total_word_lis_1 = []
for lis in text_token_1:
	for word in lis:
		total_word_lis_1.append(word)


real_words_1 = []

for word in total_word_lis_1:
    if word[0].isalpha():
    	if word != "http" and word != "https" and word != "RT":
        	real_words_1.append(word)





tweets_text_lis_2 = []
for dic in data_2:
    if "text" in dic.keys():
        tweets_text_lis_2.append(dic["text"]) 
    else:
        tweets_text_lis_2.append("")        


text_token_2 = []

for sentence in tweets_text_lis_2:
    text_token_2.append(nltk.word_tokenize(sentence))

total_word_lis_2 = []
for lis in text_token_2:
    for word in lis:
        total_word_lis_2.append(word)


real_words_2 = []

for word in total_word_lis_2:
    if word[0].isalpha():
        if word != "http" and word != "https" and word != "RT":
            real_words_2.append(word)



same_word_dict = {}
for word in real_words_1:
    if word in real_words_2:
        if word in same_word_dict:
            same_word_dict[word] += 1
        else:
            same_word_dict[word] = 1

sorted_same_word = sorted(same_word_dict.items(), key = lambda x: x[1] ,reverse=True)

five_most_freq = sorted_same_word[:5]
print(("USER 1: " + username_1 +" USER 2: " + username_2 + " TWEETS ANALYZED: " + num_tweets + " 5 MOST FREQUENT COMMON WORDS: " 
    + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" ).format(five_most_freq[0][0],five_most_freq[0][1],five_most_freq[1][0],five_most_freq[1][1],five_most_freq[2][0],five_most_freq[2][1],five_most_freq[3][0],five_most_freq[3][1],five_most_freq[4][0],five_most_freq[4][1]))










if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()




