import telebot
import api

CHAVE_API = api.api_key

bot = telebot.TeleBot(CHAVE_API)

previous_command = {}

@bot.message_handler(commands=["yareyare"]) 
def opcao1(mensagem):
    bot.send_message(mensagem,"Yare yare, pare de encher o meu saco")

@bot.message_handler(commands=["Jotaro"]) 
def opcao2(mensagem):
    bot.reply_to(mensagem,"""Sim, meu nome é Jotaro Kujo
                 /Zawarudo
                 /yare""")
    previous_command[mensagem.chat.id] = "/Jotaro"

@bot.message_handler(commands=["Dio"]) 
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id,"""Oh, você está se aproximando de mim? Em vez de fugir, você está vindo diretamente até mim?
                     /Zawarudo""")
    previous_command[mensagem.chat.id] = "/Dio"

@bot.message_handler(commands=['Zawarudo'])
def the_word_command(mensagem):
    user_id = mensagem.chat.id

    # Check the user's previous command
    if user_id in previous_command:
        previous_cmd = previous_command[user_id]
        if previous_cmd == "/Jotaro":
            # If the previous command was /jotaro, send audio
            bot.send_audio(chat_id=mensagem.chat.id, audio=open('resources/zauwarudo_jotaro.m4a', 'rb'))
        elif previous_cmd == "/Dio":
            # If the previous command was /Dio, send text
            bot.send_audio(chat_id=mensagem.chat.id, audio=open('resources/zauwarudo_dio.m4a', 'rb'))
    else:
        bot.send_message(user_id, """Selecione alguém antes
                         /Dio
                         /Jotaro""")

@bot.message_handler(commands=['yare'])
def yareyare_command(mensagem):
    user_id = mensagem.chat.id
    # Check the user's previous command
    if user_id in previous_command:
        previous_cmd = previous_command[user_id]
        if previous_cmd == "/Jotaro":
            # If the previous command was /jotaro, send audio
            bot.send_audio(chat_id=mensagem.chat.id, audio=open('resources/yareyare_jotaro_Kujo.m4a', 'rb'))
    else:
        bot.send_message(user_id, """Você selecionou alguém que não possui esse comando""")

@bot.message_handler(commands=['start'])
def start_command(mensagem):
    texto = """
    "Seja bem vindo, escolha um personagem
    /Jotaro
    /Dio"""
    bot.reply_to(mensagem, texto)
    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)  
def responder(mensagem):
    texto = """
    "Yare Yare, não entendi o que você queria dizer, escolha uma das opções por favor
    /Jotaro
    /Dio"""
    bot.reply_to(mensagem, texto)
    
bot.polling()


