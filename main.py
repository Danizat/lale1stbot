import telebot	

bot  =  telebot.TeleBot("1063033152:AAHES7oxW5ddRUKqlXkbIVEphPeswWZUn0Y")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, message.text)



bot.polling(none_stop=True)
