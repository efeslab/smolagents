import litellm 

messages = [
    {
        "role": "user",
        "content": "what llm are you"
    }
]
    
response = litellm.completion(
            model="openai/meta-llama/Llama-3.1-8B-Instruct", # pass the vllm model name
            api_key="-",
            messages=messages,
            api_base="http://127.0.0.1:8080",
            temperature=0.2,
            max_tokens=80)

print(response)