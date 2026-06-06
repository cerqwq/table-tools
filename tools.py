"""
Table Tools - AI表格工具
支持表格生成、数据处理、可视化
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class TableTools:
    """
    AI表格工具
    支持：生成、处理、可视化
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_table(self, data_description: str, columns: List[str] = None) -> str:
        """生成表格"""
        if not self.client:
            return "LLM客户端未配置"

        columns_text = ", ".join(columns) if columns else "自动推断"

        prompt = f"""请根据以下描述生成HTML表格：

描述：{data_description}
列：{columns_text}

要求：
1. 美观样式
2. 响应式设计
3. 包含示例数据
4. 可排序/筛选"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_data_table(self, data: List[Dict], features: List[str] = None) -> str:
        """生成数据表格"""
        if not self.client:
            return "LLM客户端未配置"

        data_text = json.dumps(data[:10], ensure_ascii=False)
        features_text = ", ".join(features) if features else "基本功能"

        prompt = f"""请为以下数据生成交互式表格：

数据：{data_text}
功能：{features_text}

使用React + TanStack Table："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_excel_template(self, purpose: str) -> str:
        """生成Excel模板"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{purpose}生成Excel模板的Python代码：

要求：
1. 使用openpyxl
2. 包含表头
3. 数据验证
4. 格式美化"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_table_data(self, data: List[Dict]) -> Dict:
        """分析表格数据"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(data[:20], ensure_ascii=False)

        prompt = f"""请分析以下表格数据：

{data_text}

请返回JSON格式：
{{
    "summary": "数据总结",
    "patterns": ["模式1", "模式2"],
    "statistics": {{"key": "value"}},
    "visualizations": ["建议图表1", "建议图表2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def convert_format(self, data: str, source: str, target: str) -> str:
        """转换格式"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下{source}格式数据转换为{target}格式：

{data}

只返回转换后的数据："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> TableTools:
    """创建表格工具"""
    return TableTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Table Tools")
    print()

    # 测试
    table = tools.generate_table("销售数据", ["日期", "产品", "数量", "金额"])
    print(table[:300] + "...")
