import os
import telebot
import requests
import json
import csv
import csv,io
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()


# TODO: 1.1 Get your environment variables 
yourkey = os.getenv("api_key")
bot_id = os.getenv("bot_id")

bot = telebot.TeleBot(bot_id)
s = io.StringIO()
buf = io.BytesIO()
botRunning = True
@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
   
    bot.reply_to(message, 'Getting movie info...')
    movieName = message.text
    mov = movieName[7:]
    response = requests.get(f"http://www.omdbapi.com/?apikey=1464741d&t={mov}")
    
    
    print(response.json())
    mov=response.json()
    print(mov)

    poster_url = mov['Poster']
    title = mov['Title']
    rating = mov['imdbRating']
    year = mov['Year']

    csv.writer(s).writerow([title, rating, year])
    s.seek(0)
    buf.write(s.getvalue().encode())
    buf.seek(0)
    buf.name = f'datas.csv'
    bot.send_photo(message.chat.id, poster_url, f'Title: {title}\n Year: {year}\n rating: {rating} ')

@bot.message_handler(commands=['export'])
def export(message):
    bot.send_document(message.chat.id, buf)

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
