from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import  Stream

import credentials
import json

"""
"{\"created_at\":\"Fri Mar 29 01:20:56 +0000 2019\",\"id\":1111438054969860099,\"id_str\":\"1111438054969860099\",\"text\":\"Donald Trump is turning the the peoples against us.\",\"source\":\"\\u003ca href=\\\"https:\\/\\/cheapbotsdonequick.com\\\" rel=\\\"nofollow\\\"\\u003eCheap Bots, Done Quick!\\u003c\\/a\\u003e\",\"truncated\":false,\"in_reply_to_status_id\":null,\"in_reply_to_status_id_str\":null,\"in_reply_to_user_id\":null,\"in_reply_to_user_id_str\":null,\"in_reply_to_screen_name\":null,\"user\":{\"id\":977946638135078917,\"id_str\":\"977946638135078917\",\"name\":\"Alex Jones\",\"screen_name\":\"Alex_Jones_Bot\",\"location\":null,\"url\":null,\"description\":\"Im a human!\",\"translator_type\":\"none\",\"protected\":false,\"verified\":false,\"followers_count\":9,\"friends_count\":0,\"listed_count\":0,\"favourites_count\":0,\"statuses_count\":8761,\"created_at\":\"Sun Mar 25 16:33:42 +0000 2018\",\"utc_offset\":null,\"time_zone\":null,\"geo_enabled\":false,\"lang\":\"en\",\"contributors_enabled\":false,\"is_translator\":false,\"profile_background_color\":\"F5F8FA\",\"profile_background_image_url\":\"\",\"profile_background_image_url_https\":\"\",\"profile_background_tile\":false,\"profile_link_color\":\"1DA1F2\",\"profile_sidebar_border_color\":\"C0DEED\",\"profile_sidebar_fill_color\":\"DDEEF6\",\"profile_text_color\":\"333333\",\"profile_use_background_image\":true,\"profile_image_url\":\"http:\\/\\/pbs.twimg.com\\/profile_images\\/977981241197604866\\/dOlzk9Ef_normal.jpg\",\"profile_image_url_https\":\"https:\\/\\/pbs.twimg.com\\/profile_images\\/977981241197604866\\/dOlzk9Ef_normal.jpg\",\"default_profile\":true,\"default_profile_image\":false,\"following\":null,\"follow_request_sent\":null,\"notifications\":null},\"geo\":null,\"coordinates\":null,\"place\":null,\"contributors\":null,\"is_quote_status\":false,\"quote_count\":0,\"reply_count\":0,\"retweet_count\":0,\"favorite_count\":0,\"entities\":{\"hashtags\":[],\"urls\":[],\"user_mentions\":[],\"symbols\":[]},\"favorited\":false,\"retweeted\":false,\"filter_level\":\"low\",\"lang\":\"en\",\"timestamp_ms\":\"1553822456482\"}\r\n"

"""
class TweetListener(StreamListener):
    def on_data(self, data):
        parsed_data = json.loads(data)
        print(json.dumps(parsed_data, indent=4, sort_keys=False))
        return

    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    tweet_listener = TweetListener()
    auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.acces_token_secret)
    stream = Stream(auth, tweet_listener)

    stream.filter(track=["donald trump"])


