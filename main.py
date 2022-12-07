import os
from dotenv import load_dotenv 
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    

    prompt = """
    Turn the following line from a recipe into a complete sentence:
    - add rice wok stir fry 2-3 mins when golden remove add bowl    
    
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=100
    )

    # print(response)
    return response.choices[0].text

if __name__=="__main__":
    text = main()
    print(text)