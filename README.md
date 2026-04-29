# -agent-
# 🚀 Multi-Agent 商业版智能工作台

## 项目简介

Multi-Agent 商业版智能工作台是一套基于 Python + Streamlit 开发的多智能体协同自动化系统。系统模拟企业真实协作流程，通过多个 Agent 自动完成任务规划、并发执行、结果审核与结构化输出。

适用于商业策划、创业咨询、自媒体运营、招聘提效、数据分析等场景。

---

## 核心功能

### 🤖 多 Agent 协同架构

* **Planner Agent**：理解需求并拆解任务
* **Worker Agents**：并发执行子任务
* **Reviewer Agent**：审核结果并评分

### 💼 商业场景模板

支持一键生成以下业务方案：

* 增长方案
* 创业计划书
* 自媒体运营方案
* 招聘提效方案
* 数据分析建议

### 📦 结果输出

* 页面实时展示执行日志
* 输出结构化商业方案
* 支持下载 JSON 文件

---

## 技术栈

* Python 3.10+
* Streamlit
* ThreadPoolExecutor（并发调度）

---

## 安装运行

### 1. 安装依赖

```bash
pip install streamlit
```

### 2. 启动项目

```bash
streamlit run multi_agent_mvp_app.py
```

### 3. 浏览器访问

```text
http://localhost:8501
```

---

## 使用说明

1. 打开网页后选择业务场景
2. 输入任务目标
3. 点击【运行系统】
4. 查看执行日志与最终方案
5. 下载商业结果文件

---

## 示例输入

```text
帮我做奶茶店增长方案
```

```text
开一家校园咖啡店商业计划书
```

```text
生成30天短视频运营计划
```

---

## 项目价值

* 提升复杂任务执行效率
* 降低人工协作成本
* 快速生成商业决策方案
* 可作为 AI 产品原型 / 面试作品集 / 创业项目

---

## 后续升级方向

* 接入 OpenAI / Claude / DeepSeek API
* 用户登录与付费系统
* 导出 Word / PPT / PDF
* SaaS 云端部署
* 长期记忆与智能推荐

---

## 作者说明

该项目适合作为 Multi-Agent、AI Workflow、商业自动化方向的 MVP 展示项目。
