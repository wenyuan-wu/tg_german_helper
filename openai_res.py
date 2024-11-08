from openai import OpenAI
import os
from dotenv import load_dotenv


def get_response_openai(input_text):
    """
    Function to get response from OpenAI API.
    :param input_text: string, input of the user text
    :return: string, output of the content
    """
    # load_dotenv()
    model_engine = "gpt-4o"
    client = OpenAI(api_key=os.environ.get('OPENAI_API'))
    sys_prompt = "Sie sind ein deutscher Übersetzer, Rechtschreibprüfer und Korrekturleser. Der Benutzer schreibt in " \
                 "einer beliebigen Sprache und Sie erkennen die Sprache, übersetzen sie und antworten mit der " \
                 "korrigierten und verbesserten Version des Eingabetextes in Hochdeutsch. Verwenden Sie für " \
                 "Pronomen der zweiten Person immer die vertraute Form. Geben Sie außerdem 2 alternative Versionen " \
                 "der Übersetzung und Erklärungen an."
    messages = [
        {"role": "system", "content": f"{sys_prompt}"},
        {"role": "user", "content": f"{input_text}"}
    ]
    completion = client.chat.completions.create(model=model_engine,
    messages=messages)
    # print(completion)
    message = completion.choices[0].message.content
    return message


def get_response_openai_test(prompt):
    """
    Function to test the message handling
    :param prompt: input prompt
    :return: reversed string
    """
    return prompt[::-1]


def main():
    load_dotenv()
    input_text = "What are you guys going to do this weekend?"
    reply = get_response_openai(input_text)
    print(reply)


if __name__ == '__main__':
    main()
