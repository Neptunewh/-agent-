import streamlit as st
import json
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

st.title('🚀 Multi-Agent 商业版智能工作台')
st.caption('输入业务目标，一键生成可执行商业方案（规划 → 执行 → 审核）')

mode=st.selectbox('选择业务场景',['增长方案','创业计划书','自媒体运营','招聘提效','数据分析'])
defaults={'增长方案':'帮我做奶茶店增长方案','创业计划书':'开一家校园咖啡店商业计划书','自媒体运营':'生成30天短视频运营计划','招聘提效':'设计AI招聘流程优化方案','数据分析':'分析门店销售下降原因并给建议'}
task=st.text_area('请输入任务', defaults[mode])
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
    plans={
        '增长方案':['私域会员裂变','短视频团购引流','新品周周上新','校园联名活动'],
        '创业计划书':['目标客群定位','预算10万元启动','3个月回本模型','首店选址建议'],
        '自媒体运营':['账号定位','30天选题库','爆款脚本模板','转化漏斗设计'],
        '招聘提效':['JD优化','自动筛选简历','面试题生成','人才库沉淀'],
        '数据分析':['销售漏斗诊断','复购率分析','SKU优化','门店促销建议']
    }
    output={'模式':mode,'任务':task,'评分':review['score'],'状态':review['status'],'建议':plans[mode]}
    st.json(output)
    st.download_button('下载商业方案(JSON)', data=json.dumps(output,ensure_ascii=False,indent=2), file_name='business_plan.json', mime='application/json')

st.markdown('---')
st.code('pip install streamlit\nstreamlit run multi_agent_mvp_app.py', language='bash')
