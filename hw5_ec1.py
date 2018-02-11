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




freq_dic_1 = nltk.FreqDist(real_words_1)
freq_dic_2 = nltk.FreqDist(real_words_2)
#dict_items([('QuasiCon', 3), ('Make', 1)......])

sorted_freq_1 = sorted(freq_dic_1.items(), key=lambda x: x[1], reverse = True)
sorted_freq_2 = sorted(freq_dic_2.items(), key=lambda x: x[1], reverse = True)
# [('the', 7),,,,,,,] list


sorted_freq_dict_1 = {}
for item in sorted_freq_1:
    sorted_freq_dict_1[item[0]] = item[1]
# {'Engineering': 1, ,,,,,,}  dict
# print(sorted_freq_dict_1)
sorted_freq_dict_2 = {}
for item in sorted_freq_2:
    sorted_freq_dict_2[item[0]] = item[1]
# {'Engineering': 1, ,,,,,,}  dict
# print(sorted_freq_dict_2)



word_account_1 = []
for item in sorted_freq_1:
    word_account_1.append(item[0])
#["a","b",,,,]list    


    
word_account_2 = []
for item in sorted_freq_2:
    word_account_2.append(item[0])
   


common_word = {}
for item in word_account_1:
    if item in word_account_2:
        common_word[item] = sorted_freq_dict_1[item] + sorted_freq_dict_2[item]

common_word_new = {}
common_word_lis = sorted(common_word, key=lambda x: (common_word[x],x), reverse = True)    
for item in common_word_lis:
    common_word_new[item] = common_word[item]
common_keys = list(common_word_new.keys())
print(common_word_new)


unique_word = {}
for key in common_word.keys():
    word_account_1.remove(key)
for key in common_word.keys():
    word_account_2.remove(key)
for word in word_account_1:
    unique_word[word] = sorted_freq_dict_1[word]
for word in word_account_2:
    unique_word[word] = sorted_freq_dict_2[word]
unique_word_new = {}
unique_word_lis = sorted(unique_word, key=lambda x: (unique_word[x],x), reverse = True)    
for item in unique_word_lis:
    unique_word_new[item] = unique_word[item]
unique_keys = list(unique_word_new.keys())
print(unique_word_new)



print(("USER 1: " + username_1 +" USER 2: " + username_2 + " TWEETS ANALYZED: " + num_tweets + "\n" + "5 MOST FREQUENT COMMON WORDS: " 
    + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" ).format(common_keys[0],common_word[common_keys[0]], common_keys[1],common_word[common_keys[1]], common_keys[2],common_word[common_keys[2]], common_keys[3],common_word[common_keys[3]], common_keys[4],common_word[common_keys[4]]))
print(("5 MOST FREQUENT UNIQUE WORDS: " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" + " " + "{}"+"({})" ).format(unique_keys[0],unique_word_new[unique_keys[0]], unique_keys[1],unique_word_new[unique_keys[1]], unique_keys[2],unique_word_new[unique_keys[2]], unique_keys[3],unique_word_new[unique_keys[3]], unique_keys[4],unique_word_new[unique_keys[4]]))


#final version;


if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()




