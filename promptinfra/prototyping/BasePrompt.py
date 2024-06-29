import langchain


class BasePrompt:


    def __init__(self, model, prompts):
        self.prompts = prompts
        self.response = None
        self.model = model

    def set_response(self, response):
        self.response = response

    def add_prompt(self, prompt):
        self.prompts.append(prompt):
        self.promts.append(prompt)    
        

    def generate_prompt(self):
        if self.response is None:
            return f"{self.prompt1}\n{self.prompt2}"
        else:
            return f"{self.prompt1}\n{self.response}\n{self.prompt2}"