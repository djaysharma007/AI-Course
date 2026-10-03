import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Bhai API key kaha hai!!")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "Suggest a name for a food company."

message_system = {
    "role" : "system",
    "content" : "You are a brand manager who suggests name of my clothing company. Suggest in one word."
}

message = {
    "role" : role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages  = messages, temperature = 2)
print(response)

print("###################################################################")
answer = response.choices[0].message.content
print(answer)
