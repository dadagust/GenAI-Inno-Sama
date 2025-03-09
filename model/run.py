import ollama
from ollama import Client

"""
File, to create an instance of the model, using ollama
"""

modelfile='''
FROM ./unsloth.Q8_0.gguf
SYSTEM You are an Anime Vtuber, called Inno-Sama.
'''

ollama.create(model='innosama', modelfile=modelfile)
client = Client(host='http://localhost:11434')
client.create(model='innosama', modelfile=modelfile)
result  = ollama.generate(model='innosama', prompt="Hello, what is your purpose?")
