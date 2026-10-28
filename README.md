# AlphaLens AI — Day 1

一个可运行的 Streamlit 金融分析原型。所有数据均为虚构演示数据。

## 运行步骤

1. 安装 Python 3.11 或 3.12。
2. 在本文件夹打开终端。
3. 创建虚拟环境：
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows PowerShell: `py -m venv .venv; .venv\Scripts\Activate.ps1`
4. 安装依赖：`python -m pip install -r requirements.txt`
5. 启动应用：`python -m streamlit run app.py`
6. 浏览器打开终端显示的地址，通常是 http://localhost:8501 。

## 功能
- 选择两家虚构公司
- 调整增长率、现金流率、WACC、永续增长率
- 自动计算简化 DCF 企业价值（EV）
- 查看收入与现金流图表
- AI 入口占位（Day 1 尚未接入真实模型）

## 重要限制
该版本无实时行情、真实公司财务数据、AI 推理、PDF 解析或自动部署。估值结果不是投资建议。
