# This is a sample Python script.
import json

import openai

with open('config.json') as f:
  config = json.load(f)

openai.api_key = config['key']

prompt ='say only hi'


def main():
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    print(response['choices'][0]['text'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
