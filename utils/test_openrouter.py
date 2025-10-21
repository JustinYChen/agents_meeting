#!/usr/bin/env python3
"""测试OpenRouter连接脚本"""

from llm_client import LLMClient, API_KEY, API_BASE_URL

def test_connection():
    """测试OpenRouter连接"""
    print("=== OpenRouter连接测试 ===")
    
    print(f"API Base URL: {API_BASE_URL}")
    print(f"API Key: {'已设置' if API_KEY and API_KEY != 'YOUR_OPENROUTER_API_KEY' else '未设置'}")
    
    if not API_KEY or API_KEY == 'YOUR_OPENROUTER_API_KEY':
        print("警告: API密钥未设置！")
        print("请编辑 llm_client.py 文件设置您的OpenRouter API密钥")
        return
    
    try:
        # 创建LLM客户端（使用默认配置）
        llm = LLMClient()
        
        # 测试不同的模型
        test_models = [
            "deepseek/deepseek-r1",
            "qwen/qwen3-vl-8b-thinking", 
            "anthropic/claude-3.7-sonnet",
            "google/gemini-2.5-flash"
        ]
        
        for model in test_models:
            print(f"\n--- 测试模型: {model} ---")
            messages = [
                {"role": "user", "content": "你好，这是一个连接测试。请简短回复测试是否成功。"}
            ]
            
            content, reasoning = llm.chat(messages, model=model)
            
            if content:
                print(f"[OK] {model} 连接成功！")
                print(f"响应: {content}")
                if reasoning:
                    print(f"推理内容: {reasoning[:100]}...")
            else:
                print(f"[ERROR] {model} 连接失败：没有收到响应")
                
    except Exception as e:
        print(f"[ERROR] 客户端创建失败：{str(e)}")

if __name__ == "__main__":
    test_connection()