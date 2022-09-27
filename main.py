
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN= 150
PROMISED_UP= 10
TWITTER_EMAIL= "arunna.acharya@gmail.com"
TWITTER_PASSWORD="Heyb@by5"
speed_test_link="https://www.speedtest.net/"

bot= InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL,TWITTER_PASSWORD)
