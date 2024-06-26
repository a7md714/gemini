"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import telebot
bot_token = '1981790629:AAGXe9sBFiWWhzsUaeK-8ie7AhgRnYtKV_E'
bot = telebot.TeleBot(bot_token)
def send_message(message):
    bot.send_message(message.chat.id,message)
import google.generativeai as genai
api_key="AIzaSyAdPHjXyXPd83nHepklXWrjyv9LlrvAaIo"

genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

@bot.message_handler(func=lambda message: True)
def echo_all(message):

    message_text = message.text
    chat_id = message.chat.id
    convo.send_message(message_text)
    # print()
    bot.send_message(chat_id, convo.last.text)

# Start the bot
bot.polling()
# while True:
#     text = input(" Write someThing : ")
#     if text == 'exit':
#         break
#     else:
     