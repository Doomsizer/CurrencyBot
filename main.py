from config import TOKEN, keys
from extensions import *
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def start(ctx):
    text = "Форма ввода: <название валюты> <название валюты в которую перевести> <количество>\
\nСписок доступных валют: /values"
    bot.send_message(text=text, chat_id=ctx.chat.id)


@bot.message_handler(commands=["values"])
def values(ctx):
    text = "Доступные валюты: \n"
    for i in keys.keys():
        text += f"- {i}\n"
    bot.send_message(text=text, chat_id=ctx.chat.id)


@bot.message_handler(content_types=["text", ])
def convert(ctx):
    try:
        first, second, amount = ctx.text.split(" ")
        text = Converter.convert(first, second, amount)
        bot.reply_to(ctx, str(text))
    except APIException as e:
        bot.reply_to(ctx, str(e))
    except ValueError as e:
        bot.reply_to(ctx, "Было дано неверное количество аргументов")


bot.polling(non_stop=True)
