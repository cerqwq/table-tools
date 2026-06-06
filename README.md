# 📊 Table Tools

AI表格工具，支持表格生成、数据处理、可视化。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 HTML表格生成
- 📊 数据表格生成
- 📗 Excel模板生成
- 📈 数据分析
- 🔄 格式转换

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from table_tools import create_tools

tools = create_tools()

# 生成表格
table = tools.generate_table("销售数据", ["日期", "产品", "金额"])

# 生成数据表格
data_table = tools.generate_data_table(data, ["排序", "筛选", "分页"])

# 生成Excel模板
excel = tools.generate_excel_template("财务报表")

# 分析数据
analysis = tools.analyze_table_data(data)

# 格式转换
csv = tools.convert_format(json_data, "JSON", "CSV")
```

## 📁 项目结构

```
table-tools/
├── tools.py       # 表格工具核心
└── README.md
```

## 📄 许可证

MIT License
