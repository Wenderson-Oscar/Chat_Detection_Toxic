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
    result = []
    for row in ia:
        for row1 in row:
            print(row1)
            result.append(row1)
    result = [f"{round(row['score']*100, 2)}% de ser {row['label']}" for row in result]
    await cl.Message(f"Previsão Do Comentário:\n{result}").send()
