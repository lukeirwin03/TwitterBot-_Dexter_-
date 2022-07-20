from happytransformer import HappyGeneration, GENSettings
from transformers import AutoModelForCausalLM, AutoTokenizer

def neoGPT(prompt):
    '''Method to generate and return a response to a prompt that is passed into the method using the GPT Neo Model.
    
    :param prompt: the prompt that the model generates text from.
    :type prompt: string
    :rtype: string
    :return: generated text based on the prompt given
    '''
    top_p_sampling_settings = GENSettings(do_sample=True, top_k=0, top_p=0.8, temperature=0.7, no_repeat_ngram_size=2)
    happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
    result = happy_gen.generate_text(prompt, args=top_p_sampling_settings)
    return result.text

def dialoGPT(prompt):
    '''Method to generate and return a response to a prompt that is passed into the method using the GPT Dialo Model.

    :param prompt: the prompt that the model generates text from.
    :type prompt: string
    :rtype: string
    :return: generated text based on the prompt given
    '''

    modelName = 'microsoft/DialoGPT-medium'
    tokenizer = AutoTokenizer.from_pretrained(modelName)
    model = AutoModelForCausalLM.from_pretrained(modelName)

    # encode the input and add end of string token
    input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    # generate a bot response
    chat_history_ids = model.generate(
        input_ids,
        max_length=1000,
        do_sample=True,
        top_k=100,
        temperature=0.85,
        pad_token_id=tokenizer.eos_token_id
    )
    #print the output
    output = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return output

if __name__ == '__main__':
    message = 'What is the meaning of life?'

    print(f'GPT Neo Model: {neoGPT(message)}')
    print()
    print(f'GPT Dialo Model: {dialoGPT(message)}')
    

# for later use 

# def dialoGPT():
#     modelName = 'microsoft/DialoGPT-medium'
#     tokenizer = AutoTokenizer.from_pretrained(modelName)
#     model = AutoModelForCausalLM.from_pretrained(modelName)
#     for step in range(5):
#         # take user input
#         text = input(">> You:")
#         # encode the input and add end of string token
#         input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
#         # concatenate new user input with chat history (if there is)
#         bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if step > 0 else input_ids
#         # generate a bot response
#         chat_history_ids = model.generate(
#             bot_input_ids,
#             max_length=1000,
#             do_sample=True,
#             top_k=100,
#             temperature=0.75,
#             pad_token_id=tokenizer.eos_token_id
#         )
#         #print the output
#         output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
#         print(f"DialoGPT: {output}")