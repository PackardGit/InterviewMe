import openai

configuration_message = [{}]


class GptApp:
    """
    AI application
    """
    def __init__(self):
        self.model_engine = "gpt-3.5-turbo"
        self.path_to_key = "./key/OpenAI_Key.txt"
        openai.api_key = open(self.path_to_key, "r").read().strip('\n')

    def predict(self, input_str: str, messages: list):
        """ Generate a response.
        :param: input [str]
        :return: output [str]
        """
        messages.append({"role": "user", "content": input_str})
        response = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=messages
        )
        output = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": output})
        return output, messages
