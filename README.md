# 竞赛商业计划书助手

基于 OpenAI Apps SDK / MCP 的最小可运行插件原型，提供：

- `create_outline`：生成竞赛商业计划书章节提纲
- `polish_text`：按竞赛申报风格润色文字
- `build_business_model`：生成商业模式画布九宫格基础数据

## 运行

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

服务地址：`http://localhost:8000/mcp`

开发测试时，可用 ngrok 暴露本地服务，再在 ChatGPT 的 Settings > Connectors 中添加该 MCP 地址。

## 下一步

将工具接入真实市场数据、财务计算和 Word/PDF 导出；再加入 HTML widget，即可形成完整的商业计划书助手。
