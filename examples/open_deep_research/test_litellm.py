import litellm 

messages = [
    {
        "role": "user",
        "content": "what llm are you"
    }
]
    
response = litellm.completion(
            model="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B", # pass the vllm model name
            messages=messages,
            api_base="http://0.0.0.0:8000/v1/chat/completions",
            temperature=0.2,
            max_tokens=80)

print(response)