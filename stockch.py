#-*- coding: utf-8 -*-

from chatterbot import ChatBot #importação biblioteca bot
from chatterbot.trainers import ListTrainer #importação biblioteca de aprendizado bot (machine learning)

bot = ChatBot('Célula Implantação')
trainer = ListTrainer(bot)

#criação dos diálogos
trainer.train([
    'Ola',
    'Ola,em que posso ajudar?',
    'Hoje teremos contagem de CDE?',
    'Sim, segue os proximos dias de contagem em Março: 22 ; 25 e 27  ',
    'Obrigado',
    'Agradecemos seu contato',
    'Quem é zoneti?',
    'Ele é Squad Lead do Mini-cd, um ótimo profissional e ser humano',
    'Quem é odair?',
    'Ele é analista da célula implantação e também esta aprendendo novas habilidades de desenvolvimento',
    'Quem é ayub?',
    'Um careca feio',
    'Quem é Tamara?',
    'Ela é sua esposa',
    'Meu cde travou na tela de finalização, poderia me auxiliar?',
    'Limpe os dados e o cache do aparelho e tente finalizar, se não conseguir , tente finalizar de um outro aparelho.',
    'Quem é Samanta?',
    'Ela é a PO do Mini-CD.',
    
])

while True:  # laço para a interação de perguntas e respostas do usuário e do bot
    quest = input("Você: ")
    response = bot.get_response(quest)
    print("Bot: ", response)


# conectar o chatbot ao banco de dados Mongo DB 

#storage_adapter="chatterbot.storage.MongoDatabaseAdapter"

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
#bot = ChatBot(
    #'Terminal',
    #storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    #logic_adapters=[
    #    'chatterbot.logic.BestMatch'
    #],
    #database_uri='mongodb://localhost:27017/chatterbot-database'
#)


#usar o SQL como BD:
#from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
#bot = ChatBot(
#   'SQLMemoryTerminal',
    #storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #database_uri=None,
    #logic_adapters=[
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
        #'chatterbot.logic.BestMatch'
    #]
#)

#conexão com elastic
