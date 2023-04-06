import openai
import os

# Set OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Set prompt and engine parameters
prompt = "What is the meaning of life?"
engine = "davinci"

# Generate text using the OpenAI GPT-3 API
response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=1024)

# Check if the request was successful
if response['choices'][0]['text']:
    # Print the generated text
    generated_text = response['choices'][0]['text']
    print(generated_text)
else:
    # Print error message if request was not successful
    print(f"Error: {response['error']['message']}")

