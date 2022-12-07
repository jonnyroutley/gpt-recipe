import os
from dotenv import load_dotenv 
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def complete_recipe(instruction):
    prompt = """ 
    Turn the following lines from a recipe into a complete sentence, and give the output as a numbered list in markdown format:
    {}
    """.format(instruction)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.4,
        max_tokens=1000
    )

    return response.choices[0].text

def main():
    
    with open("input.md", 'r') as input_file:
        instruction = input_file.readlines()

    response = complete_recipe(instruction)
    # md = str_to_md(response)

    return response

    

if __name__=="__main__":
    text = main()
    with open("output.md", 'w+') as file:
        file.write(text)
