from urllib import response
import chainlit as cl
from ChatBot import llm_chain

@cl.on_message
async def main(message: cl.Message):
    # Get the content of the incoming message
    incoming_message = message.content

    # Process the incoming message using falcon_chain
    response_message = llm_chain.run(incoming_message)

    # Send the response back to the user
    await cl.Message(
        content=response_message,
    ).send()

