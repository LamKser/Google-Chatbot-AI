import os

from dotenv import load_dotenv
import google.generativeai as palm

from logger import init_logger
from configs.color import ColorCode
from configs.args import argument

# Load os variable
load_dotenv()
api_key = os.getenv("Google-Generative-API-KEY")


def chatbot_response(response):
    return '[' + ColorCode.RED + "chat-bot" + ColorCode.RESET + '] ' + response

def user_response():
    return input('\t[' + ColorCode.GREEN + "user" + ColorCode.RESET + '] ')


def main():
    parser = argument()

    # Logger
    logger = init_logger(parser.log_file, mode=parser.mode)
    palm.configure(api_key=api_key)

    response = palm.chat(messages="Hi")
    logger.info(chatbot_response(response.last))

    while True:
        user = user_response()

        if user == "close":
            message = chatbot_response("See you again")
            logger.info(message)
            break
        response = response.reply(user)
        message = chatbot_response(response.last)
        logger.info(message)

if __name__ == '__main__':
    main()