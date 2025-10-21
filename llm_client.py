from openai import OpenAI
import os

# OpenRouter配置 - 直接使用API密钥
API_BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = "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"  # 请替换为您的OpenRouter API密钥

class LLMClient:
    def __init__(self, api_key=API_KEY, base_url=API_BASE_URL):
        """初始化LLM客户端"""
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
    def chat(self, messages, model="deepseek/deepseek-r1", max_retries=3):
        """与LLM交互
        
        Args:
            messages: 消息列表
            model: 使用的LLM模型
            max_retries: 最大重试次数
        
        Returns:
            tuple: (content, reasoning_content)
        """
        import time
        
        # 地区限制时的备选模型映射 - 扩展映射覆盖所有可能受限的模型
        fallback_models = {
            "openai/o3-mini": "deepseek/deepseek-r1",
            "openai/gpt-4o": "deepseek/deepseek-r1",
            "openai/gpt-4-turbo": "deepseek/deepseek-r1",
            "anthropic/claude-3.7-sonnet": "deepseek/deepseek-r1",
            "anthropic/claude-3.5-sonnet": "deepseek/deepseek-r1",
            "anthropic/claude-3-opus": "deepseek/deepseek-r1",
            "google/gemini-2.5-flash": "deepseek/deepseek-r1",
            "google/gemini-2.0-flash": "deepseek/deepseek-r1",
            "google/gemini-1.5-pro": "deepseek/deepseek-r1",
            "qwen/qwen3-vl-8b-thinking": "deepseek/deepseek-r1",
            "qwen/qwen2.5-72b": "deepseek/deepseek-r1"
        }
        
        for attempt in range(max_retries):
            try:
                print(f"LLM请求 (尝试 {attempt + 1}): {messages}")
                response = self.client.chat.completions.create(
                    model=model,
                    messages=messages,
                    extra_headers={
                        "HTTP-Referer": "https://github.com",  # Optional. Site URL for rankings on openrouter.ai.
                        "X-Title": "Agents Meeting Game",      # Optional. Site title for rankings on openrouter.ai.
                    }
                )
                if response.choices:
                    message = response.choices[0].message
                    content = message.content if message.content else ""
                    reasoning_content = getattr(message, "reasoning_content", "")
                    print(f"LLM推理内容: {content}")
                    return content, reasoning_content
                
                return "", ""
                    
            except Exception as e:
                error_msg = str(e)
                print(f"LLM调用出错 (尝试 {attempt + 1}): {error_msg}")
                
                # 检查是否是地区限制错误 - 增强检测
                is_region_error = (
                    "unsupported_country_region_territory" in error_msg or 
                    "Country, region, or territory not supported" in error_msg or
                    "Provider returned error" in error_msg and "403" in error_msg
                )
                
                if is_region_error and model in fallback_models:
                    fallback_model = fallback_models[model]
                    print(f"模型 {model} 在您的地区不可用，切换到备选模型 {fallback_model}")
                    model = fallback_model
                    continue
                
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2  # 指数退避
                    print(f"等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                else:
                    print(f"LLM调用在 {max_retries} 次尝试后失败")
                    
        return "", ""

# 使用示例
if __name__ == "__main__":
    llm = LLMClient()
    messages = [
        {"role": "user", "content": "你好"}
    ]
    response = llm.chat(messages)
    print(f"响应: {response}")