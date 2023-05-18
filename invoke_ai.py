import os
from dotenv import load_dotenv
import openai
from functools import partial
from constants import WHICH_LANGUAGE, CODE_EXPLANATION

load_dotenv()
openai.api_key = os.getenv("SECRET_KEY")


def send_question(question):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an excellent developer and a teacher",
            },
            {"role": "user", "content": question},
        ],
    )


def retrieve_answer(response):
    return response["choices"][0]["message"]["content"]


def get_code_info(question, code):
    res = send_question(f"{question}\n\n{code}")
    return retrieve_answer(res)


retrieve_code_language = partial(get_code_info, question=WHICH_LANGUAGE)
retrieve_code_explanation = partial(get_code_info, question=CODE_EXPLANATION)
