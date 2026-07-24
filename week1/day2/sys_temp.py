import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Explain time travel in Detail but under 100 words"
# SYSTEM
message_system={
    "role": "system",
    "content": "You are Buddy, an AI tutor. Always explain like teaching a beginner. If language is Hinglish,mix Hindi and English naturally. Always provide:1. Introduction 2. Theory 3. Real-life Example 4. Important Points 5. Interview Questions 6. Summary "
}
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]
# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, temperature=0)
# print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)