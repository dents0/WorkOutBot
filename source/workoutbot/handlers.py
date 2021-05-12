from workoutbot import app, bot, BOT_TOKEN
from workoutbot.workout import Workout
from workoutbot.exercises import legs_core, chest_core, back_core,  cardio_core
from workoutbot.descriptions import *
from random import choice


@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.send_message(message.chat.id, start_msg)


@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.send_message(message.chat.id, help_msg)


@bot.message_handler(commands=['about'])
def handle_command(message):
    bot.send_message(message.chat.id, about_msg)


@bot.message_handler(commands=['link'])
def handle_command(message):
    bot.send_message(message.chat.id, link_msg)


@bot.message_handler(commands=['workout_1'])
def handle_command(message):
    legs = Workout(legs_core['exercises'], legs_core['explosive'], legs_core['additional'])
    bot.send_message(message.chat.id, legs.fetch_workout(), disable_web_page_preview=True)


@bot.message_handler(commands=['workout_2'])
def handle_command(message):
    chest = Workout(chest_core['exercises'], chest_core['explosive'], chest_core['additional'])
    bot.send_message(message.chat.id, chest.fetch_workout(), disable_web_page_preview=True)


@bot.message_handler(commands=['workout_3'])
def handle_command(message):
    back = Workout(back_core['exercises'], back_core['explosive'], back_core['additional'])
    bot.send_message(message.chat.id, back.fetch_workout(), disable_web_page_preview=True)


@bot.message_handler(commands=['legs'])
def handle_command(message):
    legs = Workout(legs_core['exercises'], legs_core['explosive'], legs_core['additional'])
    bot.send_message(message.chat.id, legs.group(), disable_web_page_preview=True)


@bot.message_handler(commands=['chest'])
def handle_command(message):
    chest = Workout(chest_core['exercises'], chest_core['explosive'], chest_core['additional'])
    bot.send_message(message.chat.id, chest.group(), disable_web_page_preview=True)


@bot.message_handler(commands=['back'])
def handle_command(message):
    back = Workout(back_core['exercises'], back_core['explosive'], back_core['additional'])
    bot.send_message(message.chat.id, back.group(), disable_web_page_preview=True)


@bot.message_handler(commands=['cardio'])
def handle_command(message):
    cardio = choice(cardio_core)
    bot.send_message(message.chat.id, cardio)
