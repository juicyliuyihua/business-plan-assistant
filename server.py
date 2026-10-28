from __future__ import annotations
import os
from typing import Any
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    name="business-plan-assistant",
    stateless_http=True,
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

@mcp.tool()
def create_outline(project_name: str, industry: str, competition: str = "大学生创新创业竞赛") -> dict[str, Any]:
    """生成竞赛商业计划书的标准章节提纲。"""
    sections = [
        "项目摘要", "市场痛点与需求分析", "产品/服务方案", "技术与创新点",
        "目标市场与用户画像", "竞争格局与竞争优势", "商业模式与盈利路径",
        "市场推广与销售计划", "团队与组织架构", "实施计划与里程碑",
        "财务预测与融资计划", "风险分析与应对措施", "社会价值与可持续发展"
    ]
    return {"project_name": project_name, "industry": industry, "competition": competition, "sections": sections}

@mcp.tool()
def polish_text(text: str, tone: str = "正式、清晰、有说服力") -> dict[str, str]:
    """把一段商业计划书文字转换为竞赛申报风格的修改建议。"""
    cleaned = " ".join(text.split())
    return {
        "original": text,
        "suggested_version": cleaned,
        "style_guidance": f"保持{tone}；用数据支持判断；避免空泛形容词；每段先结论后证据。",
    }

@mcp.tool()
def build_business_model(project_name: str, customers: str, value: str, channels: str, revenue: str) -> dict[str, Any]:
    """生成商业模式画布的九宫格基础数据。"""
    return {
        "project_name": project_name,
        "customer_segments": customers,
        "value_propositions": value,
        "channels": channels,
        "customer_relationships": "线上内容触达 + 试用/咨询 + 持续服务",
        "revenue_streams": revenue,
        "key_resources": "技术、数据、团队、供应链/合作伙伴",
        "key_activities": "研发、运营、获客、交付与迭代",
        "key_partners": "高校/企业/供应商/渠道合作方",
        "cost_structure": "研发、人力、获客、生产或云服务成本",
    }

app = mcp.streamable_http_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
