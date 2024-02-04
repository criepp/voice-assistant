from openai import OpenAI

api_key="YOUR_API_KEY"

client = OpenAI(
    api_key=api_key
)

conversation_history = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Your name is Logan. Carefully heed the user's instructions."}]
print("System: You are ChatGPT, a large language model trained by OpenAI. \nYour name is Logan. Carefully heed the user's instructions.")

def response(prompt):
    user_input = prompt
    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=conversation_history,
        model="gpt-3.5-turbo",
    )

    reply_content = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply_content})

    return reply_content
