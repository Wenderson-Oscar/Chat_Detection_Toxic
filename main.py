import chainlit as cl
import requests
import environs

env = environs.Env()

API_URL = "https://api-inference.huggingface.co/models/dougtrajano/toxicity-type-detection"
headers = {"Authorization": env.str("API_KEY")}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


@cl.on_message
async def main(message: cl.Message):
    ia = query({"inputs": message.content})
    await cl.Message(ia).send()