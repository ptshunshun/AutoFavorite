import tweepy
from config import CONFIG

CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

dic = {}  # 辞書を定義しておきます。
q_list = ["プログラミング", "デイサービス"]
count = 10

for q in q_list:
    search_results = api.search(q=q, count=count)
    for result in search_results:
        if result.retweeted == False:
            text = result.text  # ツイートのテキスト部分を変数textに代入。
            id = result.id  # ツイートの識別番号を変数idに代入
            dic.update({id: text})  # 変数textと変数idの紐付けをし、辞書dicに追加。
            if '@' in dic[id]:  # 辞書dicにキーである変数idを代入し、テキスト本文を出力。＠を含むツイート（リプライ）を除外。
                pass
            else:
                api.create_favorite(id)

            # except Exception as e:
                # print(e)
