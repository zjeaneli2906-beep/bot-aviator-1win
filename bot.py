import logging
from telegram.ext import Application, CommandHandler
import random
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv('TOKEN')

async def start(update, context):
    await update.message.reply_text('Bienvenue ! Utilise /predict pour une prédiction Aviator sur 1win.')

async def predict(update, context):
    possible_multipliers = [1.2, 1.5, 2.0, 2.5, 3.0, 5.0, 10.0]
    prediction = random.choice(possible_multipliers)
    message = f"🚀 Prédiction pour la prochaine ronde Aviator (1win) : Cash out à x{prediction} !\n\nRappel : Ce n'est pas une garantie, joue responsablement."
    await update.message.reply_text(message)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('predict', predict))
    print("Bot lancé !")
    application.run_polling()

if __name__ == '__main__':
    main()
