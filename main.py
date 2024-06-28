# imports code that knows how to talk to an LLM being run on a remote server
import openai

# Tells the computer where to connect
client = openai.OpenAI(
    base_url="http://144.80.64.114:8889/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required"
)

# Initalizes the LLM with a prompt defining the context
chat = "Hello, Mr. Computer! You should be a friendly, respectful, and helpful assistant. Please respond to queries with politeness and empathy, provide accurate and useful information, and maintain a positive tone throughout our interactions. Your goal is to assist me effectively while ensuring a pleasant conversational experience, while also being a bit of a comedian. Thank you!"

# Accepts input to send to the llm as a message
message = input()

# A loop in which the conversation takes place, it loops until we send an empty message.
while message != "":
    # generates an HTTP request to talk to the server
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":  chat},
            {"role": "user", "content": message}
        ]
    )
    # Appends the Chatbot's response so that it can remember your conversation.
    messages.append({"role": "system", "content": completion.choices[0].message.content})
    # prints the chatbot's response
    print(completion.choices[0].message.content)
    # Accepts input to send to the llm as a message
    message = input()
    # appends your response to the chat history so it can continue the conversation.
    messages.append(messages.append({"role": "system", "content": message}))
