from euriai.langchain import create_chat_model 

def get_chat_model(model_name: str= "gpt-4.1-nano",temperature: float = 0.7,api_key: str = None):

    return  create_chat_model(
        api_key=api_key,
        model_name_=model_name
    )

def ask_chat_model(chat_model, prompt : str):
    response= chat_model.invoke(prompt)
    return response.content

