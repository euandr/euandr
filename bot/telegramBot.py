import telebot
from time import sleep
chave_API = "7580712470:AAF3UejXcMVh8oe5KeYMC_Kv7MMnIGUxqPc"
bot = telebot.TeleBot(chave_API)




@bot.message_handler(commands=["pizza"])  # pega a informacao e diz quando a funccao abaixo sera executada.
def pizza(mensagem):
    bot.send_message(mensagem.chat.id,"saindo pra sua casa  ")

@bot.message_handler(commands=["hamburguer"])  # pega a informacao e diz quando a funccao abaixo sera executada.
def hamburguer(mensagem):
     bot.send_message(mensagem.chat.id,"a porra ta saindo, aguarde!")

@bot.message_handler(commands=["salada"])  # pega a informacao e diz quando a funccao abaixo sera executada.
def salada(mensagem):
     txt="""
        Caso queira reclamar, entre em contato pelo zap: 
    """
     bot.send_message(mensagem.chat.id,"tem salada não!, iii, se fudeu!")
     sleep(2)
     bot.send_message(mensagem.chat.id,txt)
     sleep(2)
     bot.send_message(mensagem.chat.id,"tu acha q eu vou te dar meu zap é?")

@bot.message_handler(commands=["opcao1"])  # pega a informacao e diz quando a funccao abaixo sera executada.
def opcao1(mensagem):
     bot.send_message(mensagem.chat.id,"toma ai, escuta essa pedrada:")
     caminho=r"C:\Users\andre\OneDrive\Music\clover.mp3"
     with open(caminho, 'rb') as audio:
        bot.send_audio(mensagem.chat.id, audio)

@bot.message_handler(commands=["opcao2"])  # pega a informacao e diz quando a funccao abaixo sera executada.
def opcao2(mensagem):
    texto = """
        o que voce quer?
        temos:
        /pizza 
        /hamburguer 
        /salada
        
    """
    bot.send_message(mensagem.chat.id, texto)



@bot.message_handler(commands=["opcao3"])  # pega a informacao e diz quando a funccao abaixo sera executada.
def opcao3(mensagem):
    bot.reply_to(mensagem,"valeu! Eneas disse: Devia ter sido eu!, agora faz o L!")




def verificar(mensagem): # verificar se ha mensggem
        return True

@bot.message_handler(func=verificar)  # pega a informacao de uma funcao e diz quando a funccao abaixo sera executada.
def respostaPadrao(mensagem):
    texto="""
    Clique no item de sua escolha: 
     /opcao1 mande-me algo.
     /opcao2 fazer pedido
     /opcao3 mandar abraço pro Eneas

    Responder outra coisa nao vai funcionar,
    o cara que me criou (André), infelismente so me deu essas funcoes.
    """
    bot.reply_to(mensagem,texto)

bot.polling()  # loop