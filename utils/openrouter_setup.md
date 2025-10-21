# OpenRouter 配置指南

## API密钥配置

API密钥已直接配置在 <mcfile name="llm_client.py" path="f:\Fast_Workplace\agents_meeting\llm_client.py"></mcfile> 文件中：

```python
API_KEY = "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"
```

## 修改API密钥

如果需要更换API密钥，请直接编辑 <mcfile name="llm_client.py" path="f:\Fast_Workplace\agents_meeting\llm_client.py"></mcfile> 文件：

```python
# 将下面的值替换为您的OpenRouter API密钥
API_KEY = "your_openrouter_api_key_here"
```

## 获取OpenRouter API密钥

1. 访问 [OpenRouter](https://openrouter.ai/)
2. 注册/登录账户
3. 进入 [API Keys](https://openrouter.ai/keys) 页面
4. 创建新的API密钥

## 当前配置的模型

项目已配置以下模型（带OpenRouter提供商前缀）：

- **DeepSeek**: `deepseek/deepseek-r1`
- **ChatGPT**: `openai/o3-mini`
- **Claude**: `anthropic/claude-3.7-sonnet`
- **Gemini**: `google/gemini-2.0-flash-thinking`

## 测试连接

运行测试脚本验证配置：
```cmd
python test_openrouter.py
```

## 运行游戏

直接运行游戏，无需设置环境变量：
```cmd
python game.py
```

或者运行多局游戏：
```cmd
python multi_game_runner.py --num-games 10
```

## 模型价格参考

OpenRouter提供不同模型的价格比较，可以在 [模型页面](https://openrouter.ai/models) 查看当前价格。

## 故障排除

### 地区限制问题
如果遇到 `unsupported_country_region_territory` 错误：
- 系统会自动切换到备选的 DeepSeek 模型
- 您也可以手动修改模型配置，只使用可用的模型

### 其他连接问题
如果连接失败：
1. 检查API密钥是否正确设置
2. 确认账户有足够的余额
3. 检查网络连接
4. 查看控制台输出的详细错误信息
5. 运行测试脚本检查具体哪个模型不可用

### 模型可用性
不同地区的模型可用性：
- **DeepSeek**: 全球大部分地区可用
- **OpenAI**: 部分地区受限，会自动切换
- **Anthropic**: 部分地区受限，会自动切换  
- **Google**: 部分地区受限，会自动切换