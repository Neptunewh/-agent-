import streamlit as st
import time, random
from concurrent.futures import ThreadPoolExecutor

st.set_page_config(page_title='Multi-Agent MVP', layout='wide')

class Agent:
    def __init__(self,name): self.name=name
    def log(self,msg): return f'[{self.name}] {msg}'

class PlannerAgent(Agent):
    def run(self,task):
        return ['需求理解','信息收集','方案生成','质量检查']

class WorkerAgent(Agent):
    def run(self,subtask):
        time.sleep(random.uniform(0.5,1.2))
        return f'{subtask} 完成：输出结果已生成'

class ReviewerAgent(Agent):
    def run(self,results):
        score=random.randint(88,99)
        return {'score':score,'status':'通过' if score>=90 else '需优化','summary':'任务已完成并审核'}

class Manager:
    def __init__(self):
        self.planner=PlannerAgent('Planner')
        self.reviewer=ReviewerAgent('Reviewer')
    def execute(self,task):
        logs=[]
        subs=self.planner.run(task)
        logs.append('任务拆解完成：'+ ' / '.join(subs))
        with ThreadPoolExecutor(max_workers=4) as ex:
            workers=[WorkerAgent(f'Worker-{i+1}') for i in range(len(subs))]
            futures=[ex.submit(w.run,s) for w,s in zip(workers,subs)]
            results=[f.result() for f in futures]
        logs.extend(results)
        review=self.reviewer.run(results)
        return subs,results,review,logs

st.title('🤖 Multi-Agent 协同自动化系统 MVP')
st.caption('输入任务，一键运行 Planner → Workers → Reviewer')

task=st.text_area('请输入任务', '为公司设计 AI 自动化增长方案')
if st.button('运行系统', use_container_width=True):
    m=Manager()
    with st.spinner('多 Agent 协同执行中...'):
        subs,results,review,logs=m.execute(task)
    c1,c2,c3=st.columns(3)
    c1.metric('子任务数', len(subs))
    c2.metric('审核评分', review['score'])
    c3.metric('状态', review['status'])
    st.subheader('执行日志')
    for l in logs:
        st.write('•', l)
    st.subheader('最终结果')
    st.json(review)

st.markdown('---')
st.code('pip install streamlit\nstreamlit run multi_agent_mvp_app.py', language='bash')
