from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/default/horoscopebot/")
MODEL_PATH = "models/dialogue"
print(MODEL_PATH)
action_endpoint = EndpointConfig(url="https://horoscopebot1212-actions.herokuapp.com/webhook")
print("action_endpoint", action_endpoint)
agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)
print("agent")
input_channel = FacebookInput(
        fb_verify="my-secret-verify-token",
        # you need tell facebook this token, to confirm your URL
        fb_secret="28651269458eef5dd17d6460b506b6d2",  # your app secret
        fb_access_token="EAAJiUznmFTcBANBZBVsVbXvrP994B4njCut72yKo9ZAYch10PFvUJ8syoC3TrZBRoCLjUcjunW6fVqtvQLS7hlzVmlQmJtl92OwZABpUE6DLwYpdko7ZB8LGPpXMFRRy1DFhG1RiVZCPeAzdOxo53dVJrMDlmVUgtg0ZCLb9wLeHAZDZD"
        # token for the page you subscribed to
)
print("here")
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel],  int(os.environ.get('PORT', 5004)), serve_forever=True)
