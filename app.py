import streamlit as st

import pandas as pd

import plotly.graph_objects as go



st.set_page_config(page_title='Frida AlphaLens AI', page_icon='📈', layout='wide', initial_sidebar_state='expanded')



BG = '#101C30'

PANEL = '#17263B'

FG = '#F5F8FC'

MUTED = '#A9BCD1'

TEAL = '#6CD9CB'

BLUE = '#456EAA'

RED = '#E88787'



st.markdown("""<style>

:root { color-scheme: dark; }

.stApp, [data-testid="stAppViewContainer"] {background:#101C30; color:#F5F8FC;}

[data-testid="stHeader"] {background:rgba(16,28,48,.96);}

[data-testid="stSidebar"], [data-testid="stSidebarContent"] {background:#17263B;}

.stApp h1,.stApp h2,.stApp h3,.stApp h4,.stApp h5,.stApp h6,

.stApp p,.stApp li,.stApp label,.stApp [data-testid="stMarkdownContainer"] {color:#F5F8FC;}

[data-testid="stCaptionContainer"], [data-testid="stMetricLabel"] {color:#A9BCD1 !important;}

[data-testid="stMetricValue"] {color:#6CD9CB !important;}

.brand-subtitle {color:#A9BCD1 !important;font-size:15px;letter-spacing:1px;}

.brand-accent {color:#6CD9CB;}

/* Navigation: allow seven tabs to scroll without crushing labels */

.stTabs [data-baseweb="tab-list"] {gap:8px; overflow-x:auto; scrollbar-width:thin; scrollbar-color:#456EAA #17263B;}

.stTabs [data-baseweb="tab"] {flex-shrink:0;white-space:nowrap;color:#C1D1E3 !important;

  background:#17263B;border-radius:8px 8px 0 0;padding:10px 14px;}

.stTabs [data-baseweb="tab"]:hover {color:#F5F8FC !important;background:#213852;}

.stTabs [data-baseweb="tab"][aria-selected="true"] {color:#6CD9CB !important;background:#20394F;font-weight:700;}

.stTabs [data-baseweb="tab-highlight"] {background:#6CD9CB;}

/* All form controls and generated research conclusion */

.stApp input,.stApp textarea {color:#F5F8FC !important;background:#17263B !important;

  -webkit-text-fill-color:#F5F8FC !important;caret-color:#6CD9CB;}

.stApp textarea::placeholder,.stApp input::placeholder {color:#A9BCD1 !important;opacity:1;}

.stApp [data-baseweb="input"],.stApp [data-baseweb="textarea"],

.stApp [data-baseweb="select"] > div {background:#17263B !important;border-color:#456079 !important;color:#F5F8FC !important;}

.stApp [data-baseweb="select"] [data-testid="stMarkdownContainer"] {color:#F5F8FC;}

.stApp [data-baseweb="select"] svg {fill:#A9BCD1;}

.stApp [data-testid="stTextArea"] textarea {background:#17263B !important;color:#F5F8FC !important;

  -webkit-text-fill-color:#F5F8FC !important;line-height:1.7;border:1px solid #456079;border-radius:10px;}

.stApp [data-testid="stTextArea"] label {color:#DCE8F5 !important;}

.stApp [data-testid="stAlert"] p {color:inherit;}

.stApp [data-testid="stDownloadButton"] button {background:#25456B;color:#F5F8FC;border:1px solid #456079;}

.stApp [data-testid="stDownloadButton"] button:hover {border-color:#6CD9CB;color:#6CD9CB;}


/* Day 3.2 contrast and navigation refinements */
.stApp, .stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stMarkdownContainer"] * {color:#F5F8FC;}
.stApp .stCaptionContainer, .stApp [data-testid="stCaptionContainer"] *,
.stApp [data-testid="stMetricLabel"] * {color:#B8C9DC !important;}
.stApp [data-testid="stMetricValue"] * {color:#6CD9CB !important;}
.stApp [data-testid="stWidgetLabel"] *, .stApp label * {color:#E6EFFA !important;}
.stApp [data-testid="stTabs"] [data-baseweb="tab-list"] {flex-wrap:wrap !important;overflow:visible !important;gap:8px 10px !important;height:auto !important;}
.stApp [data-testid="stTabs"] [data-baseweb="tab"] {white-space:nowrap !important;min-height:43px !important;color:#D6E5F5 !important;}
.stApp [data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"] {color:#6CD9CB !important;}
.stApp [data-testid="stTabs"] [data-baseweb="tab-highlight"] {background:#6CD9CB !important;}
.stApp [data-testid="stTextArea"] textarea, .stApp [data-testid="stTextInput"] input {color:#F5F8FC !important;-webkit-text-fill-color:#F5F8FC !important;}
.stApp [data-testid="stDataFrame"] {border-radius:10px;overflow:hidden;}
.stApp [data-testid="stAlert"] * {color:#E8F2FF !important;}

/* Day 3.3: navigation and accessibility */
.stApp [data-testid="stRadio"] [role="radiogroup"] {gap:10px; flex-wrap:wrap;}
.stApp [data-testid="stRadio"] label {background:#20354D;border:1px solid #425B77;border-radius:10px;padding:9px 13px;}
.stApp [data-testid="stRadio"] label:has(input:checked) {background:#275267;border-color:#6CD9CB;}
.stApp [data-testid="stRadio"] label p {color:#F5F8FC !important;}
.stApp [data-testid="stCaptionContainer"] *, .stApp [data-testid="stAlert"] * {color:#D5E2F1 !important;}
.stApp [data-testid="stMetricLabel"] * {color:#D5E2F1 !important;}
.stApp [data-testid="stDataFrame"] {border:1px solid #43566B;}
</style>""", unsafe_allow_html=True)



COMPANIES = {

    '半导体公司 A（虚构）': {'revenue': 100.0, 'margin': 0.20, 'growth': 0.08},

    '清洁能源公司 B（虚构）': {'revenue': 80.0, 'margin': 0.16, 'growth': 0.12},

}



POLICIES = {

    '出口管制（假设负面冲击）': {'growth_pp': -3.0, 'margin_pp': -1.5, 'wacc_pp': 0.5, 'mechanism': '市场准入与供应链约束可能压低收入增长及现金流率，并提高风险溢价。'},

    '产业补贴（假设正面冲击）': {'growth_pp': 2.0, 'margin_pp': 1.0, 'wacc_pp': -0.3, 'mechanism': '补贴与需求支持可能改善收入和现金流表现，并降低融资风险溢价。'},

    '进口关税（假设成本冲击）': {'growth_pp': -1.0, 'margin_pp': -2.0, 'wacc_pp': 0.3, 'mechanism': '进口成本上升可能挤压现金流率，贸易不确定性也可能影响需求与资本成本。'},

}





def calculate_dcf(base_revenue, growth, margin, wacc, terminal_growth):

    if wacc <= terminal_growth:

        raise ValueError('WACC 必须高于永续增长率。')

    if growth <= -1:

        raise ValueError('收入增长率必须高于 -100%。')

    if margin < 0:

        raise ValueError('自由现金流率不能为负。')

    revenue = float(base_revenue)

    revenues, fcfs, pv_fcfs = [], [], []

    for year in range(1, 6):

        revenue *= 1 + growth

        fcf = revenue * margin

        revenues.append(revenue)

        fcfs.append(fcf)

        pv_fcfs.append(fcf / (1 + wacc) ** year)

    terminal_value = fcfs[-1] * (1 + terminal_growth) / (wacc - terminal_growth)

    pv_terminal = terminal_value / (1 + wacc) ** 5

    return {'revenues': revenues, 'fcfs': fcfs, 'pv_fcfs': pv_fcfs,

            'pv_terminal': pv_terminal, 'ev': sum(pv_fcfs) + pv_terminal}





def ev_for(g, m, w, t, revenue):

    return calculate_dcf(revenue, g, m, w, t)['ev']





def format_plot(fig, title=None, height=410):

    fig.update_layout(title=title, paper_bgcolor=BG, plot_bgcolor=PANEL,

                      font=dict(color=FG), title_font=dict(color=FG, size=18), height=height,

                      margin=dict(l=25, r=25, t=65, b=30))

    fig.update_xaxes(gridcolor='#34465B', tickfont=dict(color=MUTED), title_font=dict(color=FG))

    fig.update_yaxes(gridcolor='#34465B', tickfont=dict(color=MUTED), title_font=dict(color=FG))

    return fig





st.markdown('<h1>AlphaLens <span class="brand-accent">AI</span></h1>', unsafe_allow_html=True)

st.markdown('<p class="brand-subtitle">BY FRIDA · FINANCIAL INTELLIGENCE</p>', unsafe_allow_html=True)

st.subheader('See Beyond the Numbers.')

st.caption('From policy signals to investment insights. | Day 3.3 · Financial Research Intelligence')

st.warning('教学演示：所有公司、财务数据、政策冲击及估值假设均为虚构示例，不构成投资建议。')



with st.sidebar:

    st.header('研究设置')

    company = st.selectbox('选择研究对象', list(COMPANIES))

    base = COMPANIES[company]

    growth = st.slider('未来收入年增长率 (%)', -10, 30, int(base['growth'] * 100)) / 100

    margin = st.slider('自由现金流率 (%)', 5, 35, int(base['margin'] * 100)) / 100

    wacc = st.slider('折现率 / WACC (%)', 5, 20, 10) / 100

    terminal_growth = st.slider('永续增长率 (%)', 0.0, 4.0, 2.0, 0.5) / 100

    st.divider()

    st.subheader('情景冲击幅度')

    growth_shock = st.slider('增长率调整（百分点）', 1, 10, 4)

    margin_shock = st.slider('现金流率调整（百分点）', 1, 8, 3)

    wacc_shock = st.slider('WACC 调整（百分点）', 0.5, 3.0, 1.0, 0.5)

    st.caption('乐观：增长率和现金流率上升，WACC 下降；悲观：反向变化。')

    st.caption('货币单位：人民币亿元。')



base_result = calculate_dcf(base['revenue'], growth, margin, wacc, terminal_growth)

base_ev = base_result['ev']

scenarios = {

    'Bear': {'growth': growth - growth_shock / 100, 'margin': max(0.0, margin - margin_shock / 100), 'wacc': wacc + wacc_shock / 100},

    'Base': {'growth': growth, 'margin': margin, 'wacc': wacc},

    'Bull': {'growth': growth + growth_shock / 100, 'margin': margin + margin_shock / 100, 'wacc': wacc - wacc_shock / 100},

}

for params in scenarios.values():

    if params['wacc'] <= terminal_growth or params['margin'] < 0 or params['growth'] <= -1:
        st.error('情景参数无效：请提高 WACC 或缩小冲击幅度，使 WACC 高于永续增长率。')
        st.stop()
    params['result'] = calculate_dcf(base['revenue'], params['growth'], params['margin'], params['wacc'], terminal_growth)



st.subheader(f'研究对象：{company}')

c1, c2, c3 = st.columns(3)

c1.metric('基期收入（虚构）', f"{base['revenue']:.1f} 亿元")

c2.metric('第 5 年预测自由现金流', f"{base_result['fcfs'][-1]:.1f} 亿元")

c3.metric('基准企业价值（EV）', f'{base_ev:.1f} 亿元')



# Day 3.3: two-level navigation keeps all seven modules accessible.
NAV_GROUPS = {
    'Valuation Lab': ['📈 Financial Forecast', '🎯 Scenario Analysis', '🌡️ Sensitivity Matrix'],
    'Research Intelligence': ['🧠 Research Insights', '🔍 Value Drivers'],
    'Policy & Conclusions': ['🏛️ Policy Simulator', '📝 Research Conclusion'],
}

nav_group = st.radio('Research workspace', list(NAV_GROUPS), horizontal=True,
                     label_visibility='collapsed', key='nav_group')
active_page = st.radio('Analysis module', NAV_GROUPS[nav_group], horizontal=True,
                       label_visibility='collapsed', key=f'nav_{nav_group}')



if active_page == '📈 Financial Forecast':

    chart_df = pd.DataFrame({'年份': [f'第 {i} 年' for i in range(1, 6)],

                             '收入': base_result['revenues'], '自由现金流': base_result['fcfs']})

    fig = go.Figure()

    fig.add_trace(go.Bar(x=chart_df['年份'], y=chart_df['收入'], name='预测收入', marker_color=BLUE))

    fig.add_trace(go.Scatter(x=chart_df['年份'], y=chart_df['自由现金流'], name='预测自由现金流',

                             mode='lines+markers', line=dict(color=TEAL, width=3)))

    fig.update_layout(yaxis_title='人民币亿元')

    st.plotly_chart(format_plot(fig, '五年收入与自由现金流预测'), use_container_width=True)

    a, b = st.columns(2)

    a.metric('五年现金流现值', f"{sum(base_result['pv_fcfs']):.2f} 亿元")

    b.metric('终值现值', f"{base_result['pv_terminal']:.2f} 亿元")

    st.info('简化模型：自由现金流 = 收入 × 固定自由现金流率；EV = 五年 FCF 现值 + 终值现值。')
    terminal_share_forecast = base_result['pv_terminal'] / base_ev * 100
    if terminal_share_forecast >= 70:
        st.warning(f'终值依赖风险：终值现值占 EV 的 {terminal_share_forecast:.1f}%。估值对 WACC 和永续增长率假设较敏感。')



if active_page == '🎯 Scenario Analysis':

    rows = []

    for name in ['Bear', 'Base', 'Bull']:

        p = scenarios[name]

        rows.append({'情景': name, '收入增长率 (%)': round(p['growth'] * 100, 1),

                     '自由现金流率 (%)': round(p['margin'] * 100, 1),

                     'WACC (%)': round(p['wacc'] * 100, 1), 'EV（亿元）': round(p['result']['ev'], 2)})

    scenario_df = pd.DataFrame(rows)

    st.dataframe(scenario_df, hide_index=True, use_container_width=True)

    fig = go.Figure(go.Bar(x=scenario_df['情景'], y=scenario_df['EV（亿元）'],

                           marker_color=[RED, BLUE, TEAL], text=scenario_df['EV（亿元）'], textposition='outside'))

    fig.update_layout(yaxis_title='EV（亿元）')

    st.plotly_chart(format_plot(fig, '不同情景下的企业价值', 380), use_container_width=True)

    st.caption('情景是用户设定的假设组合，并非概率预测。')



if active_page == '🌡️ Sensitivity Matrix':

    st.subheader('WACC × 永续增长率：企业价值敏感性矩阵（亿元）')

    wacc_values = [wacc + i * 0.005 for i in range(-2, 3)]

    terminal_values = [terminal_growth + i * 0.005 for i in range(-2, 3)]

    heatmap = []

    for w in wacc_values:

        heatmap.append([None if t < 0 or w <= t else ev_for(growth, margin, w, t, base['revenue'])

                        for t in terminal_values])

    fig = go.Figure(go.Heatmap(

        z=heatmap, x=[f'{t*100:.1f}%' for t in terminal_values],

        y=[f'{w*100:.1f}%' for w in wacc_values],

        colorscale=[[0, '#25456B'], [0.5, '#357D94'], [1, TEAL]],

        text=[['N/A' if v is None else f'{v:.1f}' for v in row] for row in heatmap],

        texttemplate='%{text}', colorbar=dict(title='亿元'),

        hovertemplate='永续增长率 %{x}<br>WACC %{y}<br>EV %{z:.2f} 亿元<extra></extra>'))

    fig.update_layout(xaxis_title='永续增长率', yaxis_title='WACC')

    st.plotly_chart(format_plot(fig, height=450), use_container_width=True)

    st.caption('矩阵围绕当前假设，以 0.5 个百分点为步长变化；N/A 表示无效假设。')



if active_page == '🧠 Research Insights':

    bear_ev = scenarios['Bear']['result']['ev']

    bull_ev = scenarios['Bull']['result']['ev']

    st.subheader('规则驱动的估值洞察')

    st.write(f'基准 EV 为 **{base_ev:.2f} 亿元**；悲观情景为 **{bear_ev:.2f} 亿元**（{(bear_ev/base_ev-1)*100:+.1f}%）；乐观情景为 **{bull_ev:.2f} 亿元**（{(bull_ev/base_ev-1)*100:+.1f}%）。')

    st.write(f"终值现值占基准 EV 的 **{base_result['pv_terminal']/base_ev*100:.1f}%**。终值占比越高，估值越依赖长期增长与折现率假设。")

    st.write('情景变化同时包含增长率、现金流率和 WACC 冲击，情景间 EV 差额不能归因于某一个因素。')

    st.info('本模块基于计算规则，不是大语言模型生成。')



# Day 3: independent one-at-a-time driver analysis

DRIVER_SHOCK_PP = 1.0



def one_factor_impacts():

    definitions = [

        ('收入增长率 +1pp', growth + 0.01, margin, wacc),

        ('自由现金流率 +1pp', growth, margin + 0.01, wacc),

        ('WACC +1pp', growth, margin, wacc + 0.01),

    ]

    result = []

    for label, g, m, w in definitions:

        ev = ev_for(g, m, w, terminal_growth, base['revenue'])

        result.append({'驱动因素': label, 'EV 变化（亿元）': ev - base_ev,

                       'EV 变化 (%)': (ev / base_ev - 1) * 100})

    return pd.DataFrame(result)



driver_df = one_factor_impacts()



if active_page == '🔍 Value Drivers':

    st.subheader('单因素估值驱动分析')

    st.write('每次仅改变一个变量 **1 个百分点**，其余假设保持不变；结果用于比较局部敏感性，不代表因果识别。')

    st.dataframe(driver_df.style.format({'EV 变化（亿元）': '{:+.2f}', 'EV 变化 (%)': '{:+.2f}%'}),

                 hide_index=True, use_container_width=True)

    fig = go.Figure(go.Bar(x=driver_df['驱动因素'], y=driver_df['EV 变化（亿元）'],

                           marker_color=[TEAL if v >= 0 else RED for v in driver_df['EV 变化（亿元）']],

                           text=[f'{v:+.1f}' for v in driver_df['EV 变化（亿元）']], textposition='outside'))

    fig.update_layout(yaxis_title='EV 变化（亿元）')

    st.plotly_chart(format_plot(fig, '单因素 +1 个百分点冲击', 390), use_container_width=True)

    most_sensitive = driver_df.iloc[driver_df['EV 变化（亿元）'].abs().argmax()]

    st.write(f"在上述相同幅度的局部冲击下，绝对估值变化最大的是 **{most_sensitive['驱动因素']}**，对应 EV 变化 **{most_sensitive['EV 变化（亿元）']:+.2f} 亿元**。")

    st.caption('注意：不同变量的合理波动区间可能不同，因此相同百分点冲击不等于实际风险大小。')



if active_page == '🏛️ Policy Simulator':

    st.subheader('Policy Impact Simulator · 政策影响模拟')

    policy_name = st.selectbox('选择假设政策情景', list(POLICIES))

    policy = POLICIES[policy_name]

    st.write(f"**传导机制假设：** {policy['mechanism']}")

    st.caption('以下是演示用冲击参数，并非根据历史数据估计的政策效应。可自行调整。')

    p1, p2, p3 = st.columns(3)

    with p1:

        policy_g = st.number_input('收入增长率冲击（百分点）', -20.0, 20.0,

                                   value=float(policy['growth_pp']), step=0.5, key=f'g_{policy_name}')

    with p2:

        policy_m = st.number_input('自由现金流率冲击（百分点）', -20.0, 20.0,

                                   value=float(policy['margin_pp']), step=0.5, key=f'm_{policy_name}')

    with p3:

        policy_w = st.number_input('WACC 冲击（百分点）', -10.0, 10.0,

                                   value=float(policy['wacc_pp']), step=0.1, key=f'w_{policy_name}')

    shocked_g = growth + policy_g / 100

    shocked_m = margin + policy_m / 100

    shocked_w = wacc + policy_w / 100

    valid = shocked_g > -1 and shocked_m >= 0 and shocked_w > terminal_growth

    if not valid:

        st.error('当前政策冲击产生无效估值假设：增长率须高于 -100%，现金流率不得为负，且 WACC 必须高于永续增长率。请调整冲击参数。')

        policy_ev = None

    else:

        policy_ev = ev_for(shocked_g, shocked_m, shocked_w, terminal_growth, base['revenue'])

        delta = policy_ev - base_ev

        q1, q2, q3 = st.columns(3)

        q1.metric('基准 EV', f'{base_ev:.2f} 亿元')

        q2.metric('政策情景 EV', f'{policy_ev:.2f} 亿元')

        q3.metric('相对基准变化', f'{delta:+.2f} 亿元', f'{delta/base_ev*100:+.1f}%')

        fig = go.Figure(go.Bar(x=['基准情景', '政策情景'], y=[base_ev, policy_ev],

                               marker_color=[BLUE, TEAL if delta >= 0 else RED],

                               text=[f'{base_ev:.1f}', f'{policy_ev:.1f}'], textposition='outside'))

        st.plotly_chart(format_plot(fig, '政策假设冲击前后 EV 比较', 380), use_container_width=True)

        st.write(f'传导链条：**{policy_name} → 收入增长率 {policy_g:+.1f}pp / 现金流率 {policy_m:+.1f}pp / WACC {policy_w:+.1f}pp → EV {delta/base_ev*100:+.1f}%**。')

    st.caption('该模拟未考虑政策落地概率、时间滞后、企业应对、税务、CAPEX 或供应链动态反馈。')



if active_page == '📝 Research Conclusion':

    st.subheader('Research Conclusion Generator · 结构化研究结论')

    bear_ev = scenarios['Bear']['result']['ev']

    bull_ev = scenarios['Bull']['result']['ev']

    top = driver_df.iloc[driver_df['EV 变化（亿元）'].abs().argmax()]

    terminal_share = base_result['pv_terminal'] / base_ev * 100

    conclusion = (

        f'研究对象：{company}\n\n'

        f'一、估值概览：基准企业价值为 {base_ev:.2f} 亿元；悲观情景 {bear_ev:.2f} 亿元，'

        f'乐观情景 {bull_ev:.2f} 亿元。上述估值为简化 DCF 结果，不是股票目标价。\n\n'

        f'二、主要驱动：在单因素增加 1 个百分点的局部敏感性测试中，'

        f'{top["驱动因素"]} 对 EV 的绝对影响最大（{top["EV 变化（亿元）"]:+.2f} 亿元）。'

        f'终值现值占基准 EV 的 {terminal_share:.1f}%，需要重点检验长期增长与资本成本假设。\n\n'

        f'三、情景解释：Bear/Bull 同时调整增长、现金流率和 WACC，'

        f'因此情景之间的差异不能归因于单一变量。\n\n'

        f'四、研究局限：公司和政策数据均为虚构；模型未单独预测税收、CAPEX、'

        f'营运资本、净债务或股本数，也未纳入真实政策证据与行业可比公司。\n\n'

        f'五、后续验证：引入可追溯的财务报表和政策原文，拆解现金流预测，'

        f'检验情景假设的合理性，并与可比公司估值交叉验证。'

    )

    st.text_area('自动生成的规则化研究摘要（可复制）', conclusion, height=350, key='research_conclusion')

    st.download_button('下载研究结论 TXT', data=conclusion.encode('utf-8'),

                       file_name='AlphaLens_Day3_2_Research_Conclusion.txt', mime='text/plain')

    st.info('该结论是由计算结果和固定模板自动生成的，不是大语言模型输出，也不包含外部事实核查。')



import json
import urllib.error
import urllib.request


import json
import re
import urllib.error
import urllib.request


def verified_wacc_bridge(base, growth, margin, wacc, terminal_growth, calculate_dcf, shock_pp=1.0):
    before = calculate_dcf(base['revenue'], growth, margin, wacc, terminal_growth)
    shocked_wacc = wacc + shock_pp / 100
    after = calculate_dcf(base['revenue'], growth, margin, shocked_wacc, terminal_growth)
    five_before, five_after = sum(before['pv_fcfs']), sum(after['pv_fcfs'])
    tv_before, tv_after = before['pv_terminal'], after['pv_terminal']
    ev_delta = after['ev'] - before['ev']
    five_delta, tv_delta = five_after - five_before, tv_after - tv_before
    if abs(ev_delta - five_delta - tv_delta) > 1e-7 * max(1, abs(before['ev'])):
        raise ArithmeticError('DCF 归因未通过核对')
    return {
        'wacc_before_pct': wacc * 100, 'wacc_after_pct': shocked_wacc * 100,
        'ev_before': before['ev'], 'ev_after': after['ev'],
        'ev_delta': ev_delta,
        'ev_delta_pct': 100 * ev_delta / before['ev'] if before['ev'] else None,
        'five_before': five_before, 'five_after': five_after, 'five_delta': five_delta,
        'tv_before': tv_before, 'tv_after': tv_after, 'tv_delta': tv_delta,
        'tv_share_before_pct': 100 * tv_before / before['ev'] if before['ev'] else None,
        'tv_share_after_pct': 100 * tv_after / after['ev'] if after['ev'] else None,
        'tv_change_contribution_pct': 100 * tv_delta / ev_delta if ev_delta else None,
        'reconciliation_error': ev_delta - five_delta - tv_delta,
    }


def verify_ai_explanation(answer, bridge):
    """Conservative, incomplete rule-based screening; not semantic verification."""
    import re
    text = re.sub(r"\s+", "", answer).lower()
    warnings = []
    rules = [
        (r"(?:终值(?:现值)?占(?:ev|企业价值|总价值)(?:的)?(?:比例|比重)?|终值占比|终值比例)(?:从.{0,50})?(?:下降|降低|减少|变小).{0,55}(?:导致|造成|引起|使得|最终导致|直接导致|意味着|会使|会导致|因此|从而).{0,24}(?:dcf|ev|企业价值|估值)(?:的)?(?:下降|降低|减少)",
         "因果倒置：终值占比变化是估值组成项变化后的结果，不是本次估值下降的独立驱动。"),
        (r"(?:当|随着)?(?:终值占比|终值比例|终值现值占比)(?:下降|降低|减少)(?:时|后|，|,).{0,35}(?:dcf|ev|估值|企业价值)(?:会|将|也)?(?:下降|降低|减少)",
         "不能将终值占比下降直接解释为 DCF 估值下降的原因。"),
        (r"(?:终值占比|终值比例).{0,25}(?:决定|驱动|直接影响).{0,16}(?:dcf|ev|估值|企业价值)",
         "终值占比不是独立的估值输入变量；应说明 WACC 对各现值的影响。"),
        (r"(?:wacc|加权平均资本成本)(?:上升|提高|增加).{0,35}(?:必然|意味着|证明|说明).{0,18}(?:债务成本|融资成本|债务余额|债务)(?:上升|提高|增加)",
         "WACC 冲击不能直接推断债务成本或债务余额上升。"),
        (r"(?:终值(?:现值)?占(?:ev|企业价值)(?:的)?(?:比例|比重)?|终值占比).{0,20}(?:等于|就是|即为|代表).{0,16}(?:贡献率|变化贡献)",
         "终值占 EV 的比例不等于终值变化对 EV 变化的贡献率。"),
        (r"(?:wacc|折现率)(?:上升|提高).{0,20}(?:导致|使|造成).{0,16}(?:预测期)?(?:fcf|自由现金流)(?:本身)?(?:下降|减少)",
         "只改变 WACC 时，预测期 FCF 本身保持不变，变化的是其折现现值。"),
        (r"折现因子(?:是|为|=|：|:)(?:1/)?\(1\+wacc\)(?!\^)",
         "第 t 年的折现因子应为 1/(1+WACC)^t。"),
    ]
    for pattern, reason in rules:
        if re.search(pattern, text, re.I) and reason not in warnings:
            warnings.append(reason)

    # In this version the AI is asked not to restate numbers. Absence of numeric
    # claims is not evidence of correctness. If explicit labels occur, check them.
    expected = [
        ("基准 EV", bridge.get('ev_before'), r"基准(?:ev|企业价值)"),
        ("冲击后 EV", bridge.get('ev_after'), r"(?:冲击后|调整后)(?:ev|企业价值)"),
        ("EV 变化率", bridge.get('ev_delta_pct'), r"ev(?:变化率|变动率)"),
        ("终值变化贡献率", bridge.get('tv_change_contribution_pct'), r"终值变化(?:对ev变化的)?贡献率"),
    ]
    checks = []
    for label, expected_value, prefix in expected:
        if expected_value is None:
            continue
        match = re.search(prefix + r"[^\d%+\-]{0,12}([+\-]?\d[\d,]*(?:\.\d+)?)\s*(%)?", text)
        if match:
            value = float(match.group(1).replace(',', ''))
            percent = '率' in label
            ok = (not percent or match.group(2) == '%') and abs(value - expected_value) <= max(0.02, abs(expected_value) * 0.0001)
            checks.append((label, ok))
            if not ok:
                warnings.append(f'{label} 与 Python 结果不一致，或百分比单位缺失。')
    if not answer.strip():
        warnings.append('AI 返回空内容。')
    return checks, warnings




def verified_supplement_facts(bridge):
    """Python-owned figures, never sourced from model text."""
    return (
        f"基准 EV {bridge['ev_before']:.2f} 亿元；"
        f"冲击后 EV {bridge['ev_after']:.2f} 亿元；"
        f"EV 变化 {bridge['ev_delta_pct']:+.2f}%；"
        f"终值变化贡献率 {bridge['tv_change_contribution_pct']:.2f}%。"
    )


# Day 4.8: deterministic, machine-readable facts and conservative AI output boundaries.
def build_structured_dcf_facts(bridge):
    """Only Python calculations populate these fields; never parse them from AI text."""
    return {
        'scenario': 'WACC-only shock, all projected FCFs unchanged',
        'wacc_before_pct': round(bridge['wacc_before_pct'], 4),
        'wacc_after_pct': round(bridge['wacc_after_pct'], 4),
        'ev_before_100m_cny': round(bridge['ev_before'], 4),
        'ev_after_100m_cny': round(bridge['ev_after'], 4),
        'ev_delta_100m_cny': round(bridge['ev_delta'], 4),
        'ev_delta_pct': round(bridge['ev_delta_pct'], 4),
        'five_year_pv_delta_100m_cny': round(bridge['five_delta'], 4),
        'terminal_pv_delta_100m_cny': round(bridge['tv_delta'], 4),
        'terminal_pv_share_before_pct': round(bridge['tv_share_before_pct'], 4),
        'terminal_pv_share_after_pct': round(bridge['tv_share_after_pct'], 4),
        'terminal_delta_contribution_pct': round(bridge['tv_change_contribution_pct'], 4),
        'reconciled': abs(bridge['reconciliation_error']) < 1e-7 * max(1, abs(bridge['ev_before'])),
        'fictional_data': True,
    }


def check_ai_output_contract(answer):
    """Surface-level safety screen only, not full semantic verification."""
    import re
    warnings = []
    if len(answer) > 2400:
        warnings.append('AI 解释过长，超出补充解释长度限制。')
    # Qwen is instructed not to output numerical financial claims. Block such claims
    # rather than pretending a few regex matches can certify them.
    if re.search(r'(?<![\w])[-+]?\d+(?:\.\d+)?\s*(?:%|％|亿元|万元|亿|万|百分点|pp)', answer, re.I):
        warnings.append('AI 解释包含新的数值陈述；数值只能由 Python 可信事实区提供。')
    if re.search(r'(?:真实|实际|已证实|据报道).{0,12}(?:公司|市场|数据|政策)', answer, re.I):
        warnings.append('AI 可能把虚构研究情景描述成外部事实。')
    return warnings


# AlphaLens Day 4.9: AI research quality gate
# Heuristic screening only. This is NOT full semantic or factual verification.
def day49_quality_gate(answer):
    import re
    issues = []
    sections = re.split(r"(?m)^\s*(?:[-*]\s*)?(?:机制|需要进一步验证的假设|研究限制)\s*[：:]", answer)
    # Flag repetitive lines and near-identical enumerated claims.
    lines = [re.sub(r"^[\s\-*>\d.、（）()]+", "", x).strip() for x in answer.splitlines()]
    lines = [re.sub(r"\s+", "", x) for x in lines if len(x.strip()) >= 12]
    if len(lines) != len(set(lines)):
        issues.append('AI 解释存在重复的段落或条目。')
    # WACC-only counterfactual: share changes are outputs, not independent causal inputs.
    compact = re.sub(r"\s+", "", answer)
    causal = r"(?:导致|造成|引起|驱动|使得|使|因此|从而|决定)"
    if re.search(r"(?:终值占比|终值比例|终值现值占比).{0,35}" + causal + r".{0,35}(?:估值|EV|DCF)(?:下降|降低|减少)", compact, re.I):
        issues.append('终值占比变化不能被当作本次估值下降的独立原因。')
    if re.search(r"(?:WACC|加权平均资本成本).{0,15}(?:上升|提高|增加).{0,30}(?:债务成本|融资成本|债务余额)(?:必然|一定|同步|随之)", compact, re.I):
        issues.append('仅改变 WACC 不能证明债务成本或余额必然变化。')
    if re.search(r"(?:WACC|折现率).{0,15}(?:上升|提高).{0,20}" + causal + r".{0,12}(?:自由现金流|FCF)(?:下降|减少)", compact, re.I):
        issues.append('WACC-only 冲击不会改变预测期未折现 FCF。')
    if re.search(r"(?:唯一|完全|全部|必然|百分之百).{0,20}(?:原因|解释|归因)", compact):
        issues.append('AI 使用了缺乏充分证据的绝对因果措辞。')
    return list(dict.fromkeys(issues))

st.divider()
st.subheader('🤖 AI Research Copilot · Verified DCF')
st.caption('Day 5.0 | 结构化可信事实 · 估值审计 · AI 质量检查 · 虚构数据')

question = st.text_area(
    '输入金融或政策研究问题',
    value='为什么 WACC 从 10% 上升到 11%，会导致 DCF 估值下降？请结合终值占比解释。',
    height=105, key='verified_copilot_question',
)

shock_pp = st.number_input('WACC 冲击（百分点，相对左侧当前 WACC）', min_value=0.1, max_value=5.0,
                           value=1.0, step=0.1, key='verified_wacc_shock')
try:
    bridge = verified_wacc_bridge(base, growth, margin, wacc, terminal_growth, calculate_dcf, shock_pp)
except (ValueError, ArithmeticError, ZeroDivisionError) as exc:
    st.error(f'DCF 计算失败：{exc}')
    bridge = None

if bridge is not None:
    a, b, c = st.columns(3)
    a.metric('基准 EV', f"{bridge['ev_before']:.2f} 亿元")
    b.metric('冲击后 EV', f"{bridge['ev_after']:.2f} 亿元")
    c.metric('EV 变化', f"{bridge['ev_delta']:+.2f} 亿元",
             f"{bridge['ev_delta_pct']:+.2f}%" if bridge['ev_delta_pct'] is not None else None)
    with st.expander('查看可复核的 DCF 归因'):
        st.write(f"预测期 FCF 现值：{bridge['five_before']:.2f} → {bridge['five_after']:.2f} 亿元；变化 {bridge['five_delta']:+.2f} 亿元")
        st.write(f"终值现值：{bridge['tv_before']:.2f} → {bridge['tv_after']:.2f} 亿元；变化 {bridge['tv_delta']:+.2f} 亿元")
        st.write(f"终值现值占 EV：{bridge['tv_share_before_pct']:.2f}% → {bridge['tv_share_after_pct']:.2f}%")
        st.write(f"终值变化对 EV 变化的贡献：{bridge['tv_change_contribution_pct']:.2f}%")
        st.caption(f"归因校验误差：{bridge['reconciliation_error']:.3e} 亿元（浮点舍入误差）。")

    structured_facts = build_structured_dcf_facts(bridge)
    st.markdown('### Structured Verified Facts · 结构化可信事实')
    st.caption('以下 JSON 由 Python 计算生成，不是 AI 提取或认证；金额单位为人民币亿元。')
    with st.expander('查看机器可读事实与归因校验'):
        st.json(structured_facts)
    st.download_button('下载结构化 DCF 事实 JSON',
                       data=json.dumps(structured_facts, ensure_ascii=False, indent=2).encode('utf-8'),
                       file_name='AlphaLens_Day4_8_Verified_Facts.json', mime='application/json')

    st.markdown('### Verified Research Findings · Python 生成')
    st.write(
        f"在当前虚构公司和假设下，WACC 从 **{bridge['wacc_before_pct']:.1f}%** 上升至 "
        f"**{bridge['wacc_after_pct']:.1f}%**，EV 从 **{bridge['ev_before']:.2f} 亿元** "
        f"降至 **{bridge['ev_after']:.2f} 亿元**，变化 **{bridge['ev_delta']:+.2f} 亿元** "
        f"（**{bridge['ev_delta_pct']:+.2f}%**）。"
    )
    st.write(
        f"其中预测期五年 FCF 现值变化 **{bridge['five_delta']:+.2f} 亿元**，"
        f"终值现值变化 **{bridge['tv_delta']:+.2f} 亿元**；"
        f"后者占 EV 总变化的 **{bridge['tv_change_contribution_pct']:.2f}%**。"
    )
    st.write(
        '机制：第 t 年现金流的折现因子为 **1/(1+WACC)^t**；'
        '终值采用 **TV₅ = FCF₅ × (1+g)/(WACC−g)**，还需再折现五年。'
        '因此 WACC 上升既降低预测期现金流现值，也通过提高终值公式分母和终值折现率降低终值现值。'
    )
    st.info('本次对比仅改变 WACC；收入增长率、FCF 率、永续增长率及预测期现金流均保持不变。'
            '终值现值占 EV 的比例，不等于终值变化对 EV 变化的贡献。')

    st.markdown('### Day 5.0 · Valuation Audit Trail | 估值审计')
    st.caption('确定性 Python 检查：对比现金流现值与终值现值的变化，并核验归因加总。')
    audit_rows = [
        {'组成项': '预测期五年 FCF 现值', '基准（亿元）': bridge['five_before'],
         '冲击后（亿元）': bridge['five_after'], '变化（亿元）': bridge['five_delta']},
        {'组成项': '终值现值', '基准（亿元）': bridge['tv_before'],
         '冲击后（亿元）': bridge['tv_after'], '变化（亿元）': bridge['tv_delta']},
        {'组成项': '企业价值 EV', '基准（亿元）': bridge['ev_before'],
         '冲击后（亿元）': bridge['ev_after'], '变化（亿元）': bridge['ev_delta']},
    ]
    audit_df = pd.DataFrame(audit_rows)
    st.dataframe(audit_df.style.format({k: '{:,.4f}' for k in
                 ['基准（亿元）', '冲击后（亿元）', '变化（亿元）']}),
                 hide_index=True, use_container_width=True)
    audit_checks = {
        '基准 EV = 预测期现值 + 终值现值': abs(bridge['ev_before'] - bridge['five_before'] - bridge['tv_before']) < 1e-7,
        '冲击后 EV = 预测期现值 + 终值现值': abs(bridge['ev_after'] - bridge['five_after'] - bridge['tv_after']) < 1e-7,
        'EV 变化 = 两项现值变化之和': abs(bridge['reconciliation_error']) < 1e-7,
        'WACC 上升时 EV 不增加（本次正 FCF 假设）': bridge['ev_after'] <= bridge['ev_before'],
        '终值变化贡献率定义正确': abs(bridge['tv_change_contribution_pct'] - 100 * bridge['tv_delta'] / bridge['ev_delta']) < 1e-7,
    }
    with st.expander('查看审计规则及通过情况'):
        for label, passed in audit_checks.items():
            st.write(('✅ ' if passed else '❌ ') + label)
    if all(audit_checks.values()):
        st.success('五项确定性数值一致性检查通过（不代表外部事实认证）。')
    else:
        st.error('估值审计未通过，请检查计算逻辑；不应依赖此轮归因结果。')
    audit_export = {
        'version': 'Day 5.0', 'company': company, 'currency_unit': 'CNY 100 million',
        'fictional_data': True, 'inputs': {
            'base_revenue': base['revenue'], 'growth': growth, 'margin': margin,
            'wacc': wacc, 'terminal_growth': terminal_growth, 'wacc_shock_pp': shock_pp},
        'verified_facts': structured_facts,
        'attribution': audit_rows,
        'checks': audit_checks,
        'disclaimer': 'Deterministic model consistency only; no external factual or AI semantic verification.'
    }
    st.download_button('⬇️ 下载 Day 5.0 审计报告 JSON',
        data=json.dumps(audit_export, ensure_ascii=False, indent=2).encode('utf-8'),
        file_name='AlphaLens_Day5_Valuation_Audit.json', mime='application/json',
        key='day5_audit_export')
    st.download_button('⬇️ 下载估值归因 CSV',
        data=audit_df.to_csv(index=False).encode('utf-8-sig'),
        file_name='AlphaLens_Day5_Attribution.csv', mime='text/csv',
        key='day5_attribution_export')

    st.markdown('### Day 5.1 · Multi-Factor Valuation Bridge | 多因素估值归因')
    st.caption('按收入增长率 → FCF 率 → WACC → 永续增长率顺序逐项替换，使用精确重估；结果依赖归因顺序，并非因果识别。')
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        dg = st.number_input('收入增长率冲击（百分点）', -20.0, 20.0, 2.0, 0.5, key='d51_g')
    with c2:
        dm = st.number_input('FCF 率冲击（百分点）', -20.0, 20.0, -1.0, 0.5, key='d51_m')
    with c3:
        dw = st.number_input('WACC 冲击（百分点）', -10.0, 10.0, 1.0, 0.5, key='d51_w')
    with c4:
        dt = st.number_input('永续增长率冲击（百分点）', -4.0, 4.0, 0.0, 0.5, key='d51_t')
    before_params = [growth, margin, wacc, terminal_growth]
    after_params = [growth + dg / 100, margin + dm / 100,
                    wacc + dw / 100, terminal_growth + dt / 100]
    if after_params[0] <= -1 or after_params[1] < 0 or after_params[2] <= after_params[3] or after_params[2] <= 0:
        st.error('冲击参数无效：收入增长率须高于 -100%，FCF 率不能为负，WACC 必须为正且高于永续增长率。')
    else:
        labels = ['收入增长率', 'FCF 率', 'WACC', '永续增长率']
        states = [before_params.copy()]
        for idx in range(4):
            next_state = states[-1].copy()
            next_state[idx] = after_params[idx]
            states.append(next_state)
        values = [calculate_dcf(base['revenue'], *state)['ev'] for state in states]
        changes = [values[i + 1] - values[i] for i in range(4)]
        total_delta = values[-1] - values[0]
        residual = total_delta - sum(changes)
        wf = go.Figure(go.Waterfall(
            x=['基准 EV'] + labels + ['冲击后 EV'],
            measure=['absolute'] + ['relative'] * 4 + ['total'],
            y=[values[0]] + changes + [0],
            text=[f'{values[0]:.2f}'] + [f'{v:+.2f}' for v in changes] + [f'{values[-1]:.2f}'],
            textposition='outside',
            connector={'line': {'color': '#A9BCD1'}},
            increasing={'marker': {'color': '#6CD9CB'}},
            decreasing={'marker': {'color': '#E88787'}},
            totals={'marker': {'color': '#456EAA'}}))
        wf.update_layout(title='EV 变化瀑布图（人民币亿元）', template='plotly_dark',
                         paper_bgcolor='#101C30', plot_bgcolor='#17263B',
                         font={'color': '#F5F8FC'}, height=470,
                         margin={'l': 25, 'r': 25, 't': 70, 'b': 30},
                         yaxis_title='EV（亿元）', showlegend=False)
        st.plotly_chart(wf, use_container_width=True)
        d51_df = pd.DataFrame({
            '驱动因素': labels, '基准假设 (%)': [x * 100 for x in before_params],
            '冲击后假设 (%)': [x * 100 for x in after_params],
            'EV 变化（亿元）': changes})
        st.dataframe(d51_df.style.format({'基准假设 (%)': '{:.2f}',
                       '冲击后假设 (%)': '{:.2f}', 'EV 变化（亿元）': '{:+.4f}'}),
                       hide_index=True, use_container_width=True)
        k1, k2, k3 = st.columns(3)
        k1.metric('基准 EV', f'{values[0]:.2f} 亿元')
        k2.metric('多因素冲击后 EV', f'{values[-1]:.2f} 亿元')
        k3.metric('总变化', f'{total_delta:+.2f} 亿元',
                  f'{total_delta / values[0] * 100:+.2f}%' if values[0] else None)
        passed = abs(residual) < 1e-8 * max(1, abs(values[-1]))
        if passed:
            st.success(f'归因闭合校验通过：残差 {residual:.3e} 亿元。')
        else:
            st.error(f'归因未闭合：残差 {residual:.3e} 亿元。')
        st.caption('顺序归因会把因素交互效应分配给后进入的变量；改变替换顺序可能改变各项贡献，但不改变最终 EV。')
        d51_report = {'version': 'Day 5.1', 'fictional_data': True,
            'method': 'sequential_exact_revaluation', 'order': labels,
            'base_ev': values[0], 'final_ev': values[-1], 'delta_ev': total_delta,
            'attribution': d51_df.to_dict(orient='records'),
            'reconciliation_residual': residual, 'passed': bool(passed)}
        st.download_button('⬇️ 下载 Day 5.1 多因素归因 JSON',
            data=json.dumps(d51_report, ensure_ascii=False, indent=2).encode('utf-8'),
            file_name='AlphaLens_Day5_1_Multifactor_Attribution.json',
            mime='application/json', key='day51_json')
        st.download_button('⬇️ 下载 Day 5.1 归因 CSV',
            data=d51_df.to_csv(index=False).encode('utf-8-sig'),
            file_name='AlphaLens_Day5_1_Multifactor_Attribution.csv',
            mime='text/csv', key='day51_csv')

        st.markdown('### Day 5.2 · Shapley Valuation Attribution | 公平分摊交互效应')
        st.caption('对四项变量全部 24 种替换顺序取平均边际贡献；保留 Day 5.1 顺序归因作为对照。仅为模型情景归因，不是因果识别。')
        import itertools
        import math
        from functools import lru_cache

        # 所有 16 个混合情景必须有定义，不能只检查最终冲击参数。
        @lru_cache(maxsize=16)
        def _subset_ev(mask):
            pars = [after_params[i] if mask & (1 << i) else before_params[i] for i in range(4)]
            g_, m_, w_, t_ = pars
            if g_ <= -1 or m_ < 0 or w_ <= 0 or w_ <= t_:
                raise ValueError(f'混合情景 {mask:04b} 不满足 DCF 有效性约束')
            result = float(calculate_dcf(base['revenue'], *pars)['ev'])
            if not math.isfinite(result):
                raise ValueError('混合情景产生非有限估值')
            return result

        try:
            subset_values = [_subset_ev(mask) for mask in range(16)]
            permutations = list(itertools.permutations(range(4)))
            contributions_by_order = []
            for order in permutations:
                mask = 0
                contribution = [0.0] * 4
                for i in order:
                    next_mask = mask | (1 << i)
                    contribution[i] = _subset_ev(next_mask) - _subset_ev(mask)
                    mask = next_mask
                contributions_by_order.append(contribution)
            shapley = [sum(c[i] for c in contributions_by_order) / len(permutations) for i in range(4)]
            shapley_total = sum(shapley)
            shapley_delta = _subset_ev(15) - _subset_ev(0)
            shapley_residual = shapley_delta - shapley_total
            tolerance = 1e-8 * max(1.0, abs(shapley_delta))
            shapley_df = pd.DataFrame({
                '驱动因素': labels,
                'Day 5.1 顺序归因（亿元）': changes,
                'Day 5.2 Shapley（亿元）': shapley,
                '差异：Shapley - 顺序（亿元）': [shapley[i] - changes[i] for i in range(4)],
                '24种顺序最小贡献（亿元）': [min(c[i] for c in contributions_by_order) for i in range(4)],
                '24种顺序最大贡献（亿元）': [max(c[i] for c in contributions_by_order) for i in range(4)],
            })
            st.dataframe(shapley_df.style.format({c: '{:+.4f}' for c in shapley_df.columns if '亿元' in c}),
                         hide_index=True, use_container_width=True)
            swf = go.Figure(go.Waterfall(
                x=['基准 EV'] + labels + ['冲击后 EV'],
                measure=['absolute'] + ['relative'] * 4 + ['total'],
                y=[subset_values[0]] + shapley + [0],
                text=[f'{subset_values[0]:.2f}'] + [f'{v:+.2f}' for v in shapley] + [f'{subset_values[15]:.2f}'],
                textposition='outside',
                connector={'line': {'color': '#A9BCD1'}},
                increasing={'marker': {'color': '#6CD9CB'}},
                decreasing={'marker': {'color': '#E88787'}},
                totals={'marker': {'color': '#456EAA'}}))
            swf.update_layout(title='Shapley EV 变化瀑布图（人民币亿元）', template='plotly_dark',
                              paper_bgcolor='#101C30', plot_bgcolor='#17263B',
                              font={'color': '#F5F8FC'}, height=470,
                              margin={'l': 25, 'r': 25, 't': 70, 'b': 30},
                              yaxis_title='EV（亿元）', showlegend=False)
            st.plotly_chart(swf, use_container_width=True)
            if abs(shapley_residual) <= tolerance and abs(subset_values[0] - values[0]) <= tolerance and abs(subset_values[15] - values[-1]) <= tolerance:
                st.success(f'Shapley 归因闭合通过：24 种顺序，16 个混合情景，残差 {shapley_residual:.3e} 亿元。')
            else:
                st.error(f'Shapley 归因一致性检查未通过，残差 {shapley_residual:.3e} 亿元。')
            st.caption('Shapley 将非线性及交互效应按所有顺序的平均边际贡献分配；顺序归因与 Shapley 的差额不是单独可识别的因果交互项。')
            shapley_report = {
                'version': 'Day 5.2', 'fictional_data': True,
                'method': 'exact_shapley_average_over_24_permutations',
                'currency_unit': 'CNY 100 million',
                'labels': labels, 'base_parameters': before_params,
                'shocked_parameters': after_params,
                'base_ev': subset_values[0], 'shocked_ev': subset_values[15],
                'total_delta': shapley_delta, 'sequential_contributions': changes,
                'shapley_contributions': shapley, 'reconciliation_residual': shapley_residual,
                'all_16_subset_evs': {str(i): subset_values[i] for i in range(16)},
                'permutation_count': len(permutations),
                'passed': bool(abs(shapley_residual) <= tolerance),
                'disclaimer': 'Model attribution on fictional assumptions; not causal or externally verified.'
            }
            st.download_button('⬇️ 下载 Day 5.2 Shapley 审计 JSON',
                data=json.dumps(shapley_report, ensure_ascii=False, indent=2).encode('utf-8'),
                file_name='AlphaLens_Day5_2_Shapley_Audit.json', mime='application/json', key='day52_json')
            st.download_button('⬇️ 下载 Day 5.2 Shapley 归因 CSV',
                data=shapley_df.to_csv(index=False).encode('utf-8-sig'),
                file_name='AlphaLens_Day5_2_Shapley_Attribution.csv', mime='text/csv', key='day52_csv')
        except (ValueError, ZeroDivisionError, OverflowError) as exc:
            st.warning(f'部分混合情景无效，无法安全计算 Shapley 归因：{exc}。请调整冲击参数。')

    if st.button('✨ 生成 AI 补充解释并检查', type='primary'):
        if not question.strip():
            st.warning('请先输入研究问题。')
        else:
            st.markdown('### Python 可信事实摘要')
            st.info(verified_supplement_facts(bridge))
            facts = {'fictional': True, 'company': company, 'unit': '亿元人民币',
                     'revenue_growth_pct': growth * 100, 'fcf_margin_pct': margin * 100,
                     'terminal_growth_pct': terminal_growth * 100, 'computed': bridge}
            prompt = (
                '你是金融研究助理。可信计算事实已由 Python 单独展示。'
                '不要复述、重新计算或修改 EV、百分比和归因数字。'
                '你只需用简洁中文解释机制、补充可检验的研究假设和研究限制。'
                '当前模型仅外生改变 WACC，不能推断债务成本、债务余额或资本结构必然变化。'
                '严格区分终值现值占 EV 比例与终值变化对 EV 变化的贡献率。'
                '第 t 年折现因子是 1/(1+WACC)^t；终值为 FCF5*(1+g)/(WACC-g)，再折现五年。'
                '不得创造外部事实或把虚构公司说成真实公司。'
                '若用户问题与 DCF 情景无关，请明确说明当前资料不足，不要强行回答。'
                '只输出三个小节：机制、需要进一步验证的假设、研究限制。'
                '\n可信计算 JSON（仅供理解，不要复述数字）：\n'
                + json.dumps(facts, ensure_ascii=False) + '\n用户问题：' + question
            )
            payload = {'model': 'qwen2.5:1.5b', 'prompt': prompt, 'stream': False,
                       'options': {'temperature': 0.1, 'num_predict': 550}}
            try:
                with st.spinner('正在生成补充解释并执行风险检查...'):
                    req = urllib.request.Request(
                        'http://127.0.0.1:11434/api/generate',
                        data=json.dumps(payload).encode('utf-8'),
                        headers={'Content-Type': 'application/json'}, method='POST')
                    with urllib.request.urlopen(req, timeout=180) as resp:
                        raw = json.loads(resp.read().decode('utf-8'))
                answer = raw.get('response', '').strip()
                if not answer:
                    st.warning('模型没有返回内容；Python 可信结论不受影响。')
                else:
                    checks, warnings = verify_ai_explanation(answer, bridge)
                    warnings.extend(check_ai_output_contract(answer))
                    warnings.extend(day49_quality_gate(answer))
                    warnings = list(dict.fromkeys(warnings))
                    if warnings:
                        st.warning('AI 补充解释触发启发式风险检查，已隐藏解释；Python 计算结果仍可查看。')
                        with st.expander('查看检查原因与 AI 原文（仅供排错）'):
                            for issue in warnings:
                                st.write('- ' + issue)
                            st.code(answer, language='markdown')
                    else:
                        st.markdown('### AI 补充解释 · 仅通过启发式检查（未经事实认证）')
                        st.markdown(answer)
                        st.caption('仅通过有限规则检查，并非事实认证或完整语义验证。')
                        with st.expander('查看文本匹配细节'):
                            st.write(f'发现带标签的数值陈述：{len(checks)} 项；'
                                     f'其中匹配 Python 结果：{sum(ok for _, ok in checks)} 项。')
                    st.caption('所有可信数值以 Python Verified Research Findings 为准；'
                               '本地 AI 未接入外部研究资料。')
            except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
                st.warning('AI 暂时不可用，已保留 Python 可信结论。')
                with st.expander('技术详情'):
                    st.code(str(exc))

# Day 5.3 · Monte Carlo Valuation & Downside Risk
st.markdown('## Day 5.3 · Monte Carlo Valuation & Downside Risk | 概率估值与下行风险')
st.caption('基于当前侧边栏 DCF 假设进行联合情景模拟；这是用户设定的概率模型，不是经市场数据校准的真实预测。')
with st.expander('⚙️ 设置模拟参数', expanded=True):
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        mc_n = st.select_slider('模拟次数', options=[1000, 3000, 5000, 10000, 20000], value=5000)
        mc_seed = st.number_input('随机种子', min_value=0, max_value=999999, value=42, step=1)
    with mc2:
        mc_growth_sd = st.number_input('收入增长率标准差（百分点）', min_value=0.0, max_value=20.0, value=3.0, step=0.5)
        mc_margin_sd = st.number_input('FCF 率标准差（百分点）', min_value=0.0, max_value=15.0, value=2.0, step=0.5)
    with mc3:
        mc_wacc_sd = st.number_input('WACC 标准差（百分点）', min_value=0.0, max_value=10.0, value=1.0, step=0.25)
        mc_terminal_sd = st.number_input('永续增长率标准差（百分点）', min_value=0.0, max_value=3.0, value=0.5, step=0.25)
    st.caption('四个冲击独立抽样、服从正态分布；无效情景剔除，不进行悄悄截断。若 WACC 接近永续增长率，估值可能出现极端右尾。')

import numpy as np
rng53 = np.random.default_rng(int(mc_seed))
means53 = np.array([growth, margin, wacc, terminal_growth], dtype=float)
sds53 = np.array([mc_growth_sd, mc_margin_sd, mc_wacc_sd, mc_terminal_sd]) / 100.0
samples53 = rng53.normal(means53, sds53, size=(int(mc_n), 4))
g53, m53, w53, t53 = samples53.T
valid53 = (g53 > -1) & (m53 >= 0) & (w53 > 0) & (t53 > -1) & (w53 > t53 + 0.001)
valid_count53 = int(valid53.sum())
if valid_count53 < max(100, int(mc_n * 0.5)):
    st.error(f'仅 {valid_count53}/{mc_n} 个情景有效，无法提供稳定的风险摘要。请调整假设或波动率。')
else:
    g53, m53, w53, t53 = [v[valid53] for v in (g53, m53, w53, t53)]
    years53 = np.arange(1, 6)
    revenue53 = float(base['revenue']) * (1 + g53[:, None]) ** years53
    fcf53 = revenue53 * m53[:, None]
    pv53 = (fcf53 / (1 + w53[:, None]) ** years53).sum(axis=1)
    terminal53 = fcf53[:, -1] * (1 + t53) / (w53 - t53) / (1 + w53) ** 5
    ev53 = pv53 + terminal53
    baseline53 = calculate_dcf(base['revenue'], growth, margin, wacc, terminal_growth)['ev']
    p10, p50, p90 = np.percentile(ev53, [10, 50, 90])
    loss_prob53 = float(np.mean(ev53 < baseline53))
    cols53 = st.columns(4)
    cols53[0].metric('P10 · 下侧分位', f'{p10:,.2f} 亿元')
    cols53[1].metric('P50 · 中位估值', f'{p50:,.2f} 亿元')
    cols53[2].metric('P90 · 上侧分位', f'{p90:,.2f} 亿元')
    cols53[3].metric('低于当前基准 EV 的比例', f'{loss_prob53:.1%}')
    st.caption(f'有效情景 {valid_count53:,}/{mc_n:,}（剔除 {mc_n-valid_count53:,}）；P10/P90 是模拟分位数，不代表置信区间。')
    fig53 = go.Figure()
    fig53.add_trace(go.Histogram(x=ev53, nbinsx=65, name='模拟 EV', marker_color='#6CD9CB'))
    fig53.add_vline(x=baseline53, line_dash='dash', line_color='#F5F8FC', annotation_text='基准 EV')
    fig53.add_vline(x=p50, line_dash='dot', line_color='#F2BC6B', annotation_text='P50')
    fig53.update_layout(title='模拟企业价值分布（人民币亿元）', template='plotly_dark',
                        paper_bgcolor='#101C30', plot_bgcolor='#17263B', font_color='#F5F8FC',
                        xaxis_title='EV（亿元）', yaxis_title='情景数', bargap=0.04,
                        margin=dict(l=20, r=20, t=65, b=30))
    st.plotly_chart(fig53, use_container_width=True)
    with st.expander('查看参数分布与诊断'):
        diag53 = pd.DataFrame({'参数': ['收入增长率', 'FCF 率', 'WACC', '永续增长率'],
            '输入均值 (%)': means53 * 100, '输入标准差（百分点）': sds53 * 100,
            '有效样本均值 (%)': [np.mean(v)*100 for v in (g53,m53,w53,t53)]})
        st.dataframe(diag53.round(3), use_container_width=True, hide_index=True)
        st.caption('剔除无效抽样后，实际分布可能偏离输入均值。此处尚未建模变量相关性或时间序列波动。')
    export53 = pd.DataFrame({'revenue_growth':g53, 'fcf_margin':m53, 'wacc':w53,
                             'terminal_growth':t53, 'pv_forecast_fcf':pv53,
                             'pv_terminal':terminal53, 'ev_100m_cny':ev53})
    st.download_button('⬇️ 下载 Day 5.3 Monte Carlo 模拟 CSV',
        export53.to_csv(index=False).encode('utf-8-sig'),
        file_name='AlphaLens_Day5_3_Monte_Carlo.csv', mime='text/csv', key='day53_csv')
    audit53 = {'version':'Day 5.3', 'fictional_data':True, 'seed':int(mc_seed),
               'draws':int(mc_n), 'valid_draws':valid_count53, 'baseline_ev':float(baseline53),
               'p10':float(p10), 'p50':float(p50), 'p90':float(p90),
               'probability_below_baseline':loss_prob53,
               'distribution':'independent Gaussian; invalid draws excluded',
               'sd_percentage_points':sds53.tolist()}
    st.download_button('⬇️ 下载 Day 5.3 风险审计 JSON',
        json.dumps(audit53, ensure_ascii=False, indent=2).encode('utf-8'),
        file_name='AlphaLens_Day5_3_Risk_Audit.json', mime='application/json', key='day53_json')


    # Day 5.4 · risk diagnostics and validation (conditional on sufficient valid draws)
    st.markdown('## Day 5.4 · Risk Diagnostics & Model Validation | 风险诊断与模型验证')
    st.caption('以下均为假设分布下的模型情景风险，不代表市场概率、统计置信区间或可交易资产的 VaR。')
    loss54 = baseline53 - ev53
    var90_54 = float(np.quantile(loss54, 0.90))
    var95_54 = float(np.quantile(loss54, 0.95))
    cvar95_54 = float(np.mean(loss54[loss54 >= var95_54]))
    threshold54 = float(baseline53 * 0.80)
    prob20_54 = float(np.mean(ev53 < threshold54))
    r54 = st.columns(4)
    r54[0].metric('90% 情景损失分位', f'{var90_54:,.2f} 亿元')
    r54[1].metric('95% 情景损失分位', f'{var95_54:,.2f} 亿元')
    r54[2].metric('最差 5% 平均损失', f'{cvar95_54:,.2f} 亿元')
    r54[3].metric('EV 低于基准 80% 的比例', f'{prob20_54:.1%}')
    st.caption('损失定义为基准 EV − 模拟 EV；正值表示相对基准的估值损失，负值表示估值上升。')
    with st.expander('🔍 分布尾部与抽样有效性诊断', expanded=True):
        gap54 = w53 - t53
        q54 = np.quantile(ev53, [0.01, 0.05, 0.5, 0.95, 0.99])
        diag54 = pd.DataFrame({'指标':['有效率','WACC−g 最小差距（百分点）','EV P1','EV P5','EV P50','EV P95','EV P99','最大 EV / P99'],
          '数值':[f'{valid_count53/mc_n:.2%}', f'{gap54.min()*100:.3f}', *[f'{x:,.2f} 亿元' for x in q54], f'{ev53.max()/max(q54[-1],1e-12):.2f}×']})
        st.dataframe(diag54, hide_index=True, use_container_width=True)
        if valid_count53/mc_n < 0.95:
            st.warning('超过 5% 的原始抽样被剔除：结果是条件于有效抽样的分布，可能存在选择偏差。')
        if np.mean(gap54 < 0.02) > 0.01 or ev53.max() > 3*q54[-1]:
            st.warning('检测到 WACC 与永续增长率接近或极端右尾；请降低波动率、重新校准分布或考虑经济上合理的约束。')
        st.info('当前四个参数独立抽样，未校准相关性；下方仅展示有效样本的经验相关性，不代表经济变量之间真实相关性。')
        corr54 = pd.DataFrame(np.column_stack([g53,m53,w53,t53]), columns=['收入增长率','FCF率','WACC','永续增长率']).corr()
        st.dataframe(corr54.style.format('{:.3f}'), use_container_width=True)
    with st.expander('🧪 随机种子稳定性检查（重复模拟）'):
        st.caption('以相同假设、不同随机种子重复计算 P10/P50/P90；该检查衡量蒙特卡洛抽样误差，不检验模型假设是否正确。')
        repetitions54 = st.select_slider('独立重复次数', options=[3,5,10], value=5, key='repetitions54')
        rows54=[]
        for i54 in range(repetitions54):
            rg54=np.random.default_rng(int(mc_seed)+1000+i54)
            sm54=rg54.normal(means53,sds53,size=(int(mc_n),4))
            gg54,mm54,ww54,tt54=sm54.T
            ok54=(gg54 > -1)&(mm54 >= 0)&(ww54 > 0)&(tt54 > -1)&(ww54 > tt54+0.001)
            if ok54.sum() < max(100,int(mc_n*0.5)):
                rows54.append({'重复':i54+1,'有效样本':int(ok54.sum()),'P10':np.nan,'P50':np.nan,'P90':np.nan})
                continue
            gg54,mm54,ww54,tt54=sm54[ok54].T
            ff54=float(base['revenue'])*(1+gg54[:,None])**years53*mm54[:,None]
            vals54=(ff54/(1+ww54[:,None])**years53).sum(axis=1)+ff54[:,-1]*(1+tt54)/(ww54-tt54)/(1+ww54)**5
            quant54=np.quantile(vals54,[0.1,0.5,0.9])
            rows54.append({'重复':i54+1,'有效样本':len(vals54),'P10':quant54[0],'P50':quant54[1],'P90':quant54[2]})
        repeats_df54=pd.DataFrame(rows54)
        st.dataframe(repeats_df54.style.format({'P10':'{:.2f}','P50':'{:.2f}','P90':'{:.2f}'}), use_container_width=True, hide_index=True)
        for label54 in ['P10','P50','P90']:
            values54=repeats_df54[label54].dropna()
            if len(values54)>1:
                st.write(f'{label54} 跨种子范围：{values54.min():,.2f}–{values54.max():,.2f} 亿元；标准差 {values54.std(ddof=1):.2f} 亿元')
    audit54={'version':'Day 5.4','fictional_data':True,'seed':int(mc_seed),'draws':int(mc_n),
             'valid_draws':int(valid_count53),'baseline_ev_100m_cny':float(baseline53),
             'p10':float(p10),'p50':float(p50),'p90':float(p90),
             'loss_var90_100m_cny':var90_54,'loss_var95_100m_cny':var95_54,
             'loss_cvar95_100m_cny':cvar95_54,'prob_ev_below_80pct_baseline':prob20_54,
             'validity_rate':float(valid_count53/mc_n),'minimum_wacc_minus_g':float(gap54.min()),
             'assumptions':'independent normal draws; invalid draws discarded; conditional distribution; fictional model'}
    st.download_button('⬇️ 下载 Day 5.4 风险诊断 JSON',json.dumps(audit54,ensure_ascii=False,indent=2).encode('utf-8'),
        file_name='AlphaLens_Day5_4_Risk_Diagnostics.json',mime='application/json',key='day54_audit')




# Day 5.5 · Correlated Monte Carlo & Joint Stress Testing
st.divider()
st.markdown('## Day 5.5 · Correlated Monte Carlo & Stress Testing | 相关性模拟与联合压力测试')
st.caption('保留 Day 5.3 独立正态抽样作为基准；本模块引入用户设定的相关性，并比较同一组边际假设下的风险差异。相关系数及压力冲击未经市场数据校准。')

D55_NAMES = ['收入增长率', 'FCF 率', 'WACC', '永续增长率']
D55_PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
D55_DEFAULTS = [0.40,-0.30,0.10,-0.25,0.10,0.20]


def d55_simulate(z, means, sds, corr, revenue, baseline):
    # Same standard-normal innovations across scenarios: common random numbers.
    eigval, eigvec = np.linalg.eigh(corr)
    if np.min(eigval) < -1e-8:
        raise ValueError('相关矩阵不是半正定矩阵，无法进行联合正态抽样。')
    root = eigvec @ np.diag(np.sqrt(np.maximum(eigval, 0.0))) @ eigvec.T
    draws = means + (z @ root.T) * sds
    g, m, w, t = draws.T
    valid = (g > -1) & (m >= 0) & (w > 0) & (t > -1) & (w > t + 0.001)
    ev = np.full(len(z), np.nan)
    if np.any(valid):
        gg, mm, ww, tt = draws[valid].T
        years = np.arange(1,6)
        fcfs = revenue * (1 + gg[:,None]) ** years * mm[:,None]
        pv = np.sum(fcfs / (1 + ww[:,None]) ** years, axis=1)
        tv = fcfs[:,-1] * (1 + tt) / (ww - tt) / (1 + ww) ** 5
        ev[valid] = pv + tv
        valid &= np.isfinite(ev)
        ev[~valid] = np.nan
    good = ev[valid]
    if len(good) < max(100, int(0.5 * len(z))):
        raise ValueError(f'有效样本不足：{len(good)}/{len(z)}。请调整相关性或标准差。')
    loss = baseline - good
    q95 = np.quantile(loss, 0.95)
    return {'draws':draws, 'valid':valid, 'ev':ev, 'good':good,
            'valid_rate':float(valid.mean()), 'p10':float(np.quantile(good,.1)),
            'p50':float(np.median(good)), 'p90':float(np.quantile(good,.9)),
            'loss_p95':float(q95), 'tail_mean95':float(loss[loss >= q95].mean()),
            'prob_below_base':float(np.mean(good < baseline)),
            'prob_below_80':float(np.mean(good < baseline * .8))}

with st.expander('⚙️ 相关性与联合模拟设置', expanded=True):
    st.write('设置六组两两相关系数（-1 到 +1）；对角线固定为 1。')
    d55_corr = np.eye(4)
    d55_cols = st.columns(3)
    for k, (i,j) in enumerate(D55_PAIRS):
        with d55_cols[k%3]:
            val = st.number_input(f'{D55_NAMES[i]} × {D55_NAMES[j]}',
                    min_value=-0.99, max_value=0.99, value=D55_DEFAULTS[k], step=0.05,
                    format='%.2f', key=f'd55_corr_{i}_{j}')
        d55_corr[i,j] = d55_corr[j,i] = float(val)
    d55_seed = st.number_input('Day 5.5 随机种子', min_value=0, max_value=999999,
                               value=int(mc_seed), step=1, key='d55_seed')
    d55_n = st.select_slider('Day 5.5 抽样次数', options=[1000,3000,5000,10000,20000],
                             value=int(mc_n), key='d55_n')
    st.dataframe(pd.DataFrame(d55_corr, index=D55_NAMES, columns=D55_NAMES).style.format('{:.2f}'),
                 use_container_width=True)

baseline55 = float(base_ev)
eig55 = np.linalg.eigvalsh(d55_corr)
if eig55.min() < -1e-8:
    st.error(f'相关性矩阵无效：最小特征值 {eig55.min():.4f} < 0。请降低冲突的相关系数；系统不会自动悄悄修正矩阵。')
else:
    if eig55.min() < 1e-6:
        st.warning('相关矩阵接近奇异；结果可能对相关系数微调敏感。')
    st.success(f'相关矩阵半正定检查通过（最小特征值 {eig55.min():.4f}）。')
    d55_rng = np.random.default_rng(int(d55_seed))
    d55_z = d55_rng.standard_normal((int(d55_n),4))
    try:
        d55_ind = d55_simulate(d55_z, means53, sds53, np.eye(4), float(base['revenue']), baseline55)
        d55_cor = d55_simulate(d55_z, means53, sds53, d55_corr, float(base['revenue']), baseline55)
    except ValueError as exc:
        st.error(str(exc))
    else:
        d55_metrics = [
            ('P10 EV（亿元）','p10'), ('P50 EV（亿元）','p50'),
            ('P90 EV（亿元）','p90'), ('95% 情景损失分位（亿元）','loss_p95'),
            ('最差 5% 平均损失（亿元）','tail_mean95'),
            ('EV 低于基准比例','prob_below_base'),
            ('EV 低于基准 80% 比例','prob_below_80'), ('有效率','valid_rate')]
        d55_comparison = pd.DataFrame([
            {'风险指标':label, '独立抽样':d55_ind[key], '相关抽样':d55_cor[key],
             '差异（相关−独立）':d55_cor[key]-d55_ind[key]}
            for label,key in d55_metrics])
        st.markdown('### 独立 vs 相关抽样：风险对比')
        st.dataframe(d55_comparison.style.format({
            '独立抽样':'{:.4f}', '相关抽样':'{:.4f}', '差异（相关−独立）':'{:+.4f}'}),
            hide_index=True, use_container_width=True)
        st.caption('最后三项中的概率及有效率采用 0–1 小数表示。两组使用相同标准正态随机数以降低比较噪声；剔除无效样本后，结果均为条件分布。')
        plot55 = go.Figure()
        plot55.add_trace(go.Histogram(x=d55_ind['good'], histnorm='probability density',
                                      nbinsx=65, opacity=.55, name='独立抽样', marker_color=BLUE))
        plot55.add_trace(go.Histogram(x=d55_cor['good'], histnorm='probability density',
                                      nbinsx=65, opacity=.55, name='相关抽样', marker_color=TEAL))
        plot55.add_vline(x=baseline55, line_color='#F2BC6B', line_dash='dash')
        plot55.update_layout(barmode='overlay', xaxis_title='EV（亿元）', yaxis_title='概率密度')
        st.plotly_chart(format_plot(plot55, 'EV 分布对比：相关性如何改变尾部风险', 450), use_container_width=True)
        with st.expander('🔎 抽样后相关性与有效性诊断'):
            empirical55 = pd.DataFrame(d55_cor['draws'][d55_cor['valid']], columns=D55_NAMES).corr()
            st.dataframe(empirical55.style.format('{:.3f}'), use_container_width=True)
            st.write(f"独立抽样有效率：{d55_ind['valid_rate']:.2%}；相关抽样有效率：{d55_cor['valid_rate']:.2%}。")
            st.caption('展示的是剔除无效情景后的经验相关系数，不一定等于输入矩阵；正态分布与相关性均为假设。')
            if min(d55_ind['valid_rate'], d55_cor['valid_rate']) < .95:
                st.warning('有效率低于 95%，条件筛选可能明显改变尾部分布。')
        d55_samples = pd.DataFrame({
            'independent_ev_100m_cny':d55_ind['ev'], 'correlated_ev_100m_cny':d55_cor['ev'],
            'independent_valid':d55_ind['valid'], 'correlated_valid':d55_cor['valid']})
        st.download_button('⬇️ 下载 Day 5.5 联合模拟 CSV',
            d55_samples.to_csv(index=False).encode('utf-8-sig'),
            file_name='AlphaLens_Day5_5_Correlated_MC.csv', mime='text/csv', key='d55_csv')
        d55_report = {'version':'Day 5.5', 'fictional_data':True,
            'model':'user_assumed_correlated_multivariate_normal',
            'seed':int(d55_seed), 'draws':int(d55_n),
            'parameter_names':D55_NAMES, 'means':means53.tolist(), 'standard_deviations':sds53.tolist(),
            'correlation_matrix':d55_corr.tolist(), 'minimum_eigenvalue':float(eig55.min()),
            'baseline_ev_100m_cny':baseline55,
            'independent':{k:v for k,v in d55_ind.items() if isinstance(v,float)},
            'correlated':{k:v for k,v in d55_cor.items() if isinstance(v,float)},
            'disclaimer':'Fictional scenario model, not calibrated probabilities or tradable VaR.'}
        st.download_button('⬇️ 下载 Day 5.5 相关性风险审计 JSON',
            json.dumps(d55_report,ensure_ascii=False,indent=2).encode('utf-8'),
            file_name='AlphaLens_Day5_5_Correlation_Audit.json',mime='application/json',key='d55_json')

st.markdown('### Joint Stress Testing | 联合压力测试')
st.caption('以下为确定性联合冲击，不是蒙特卡洛分位数；可用于观察不利因素同时发生时的估值变化。')
stress55 = {
    '温和下行':[-2.0,-1.0,0.5,-0.2],
    '严重衰退':[-6.0,-3.0,2.0,-0.5],
    '融资收紧':[-1.0,-0.5,3.0,-0.5],
    '需求反弹':[3.0,1.5,-0.5,0.2],
}
stress_rows55=[]
for name55, shocks55 in stress55.items():
    params55 = means53 + np.array(shocks55)/100
    g55,m55,w55,t55=params55
    if g55 <= -1 or m55 < 0 or w55 <= 0 or t55 <= -1 or w55 <= t55:
        stress_rows55.append({'情景':name55,'增长冲击(pp)':shocks55[0], 'FCF冲击(pp)':shocks55[1],
                              'WACC冲击(pp)':shocks55[2], '永续增长冲击(pp)':shocks55[3],
                              'EV（亿元）':np.nan, 'EV变化(%)':np.nan, '状态':'无效参数'})
        continue
    stress_ev55 = float(ev_for(g55,m55,w55,t55,float(base['revenue'])))
    stress_rows55.append({'情景':name55,'增长冲击(pp)':shocks55[0], 'FCF冲击(pp)':shocks55[1],
                          'WACC冲击(pp)':shocks55[2], '永续增长冲击(pp)':shocks55[3],
                          'EV（亿元）':stress_ev55, 'EV变化(%)':100*(stress_ev55/baseline55-1), '状态':'有效'})
stress_df55 = pd.DataFrame(stress_rows55)
st.dataframe(stress_df55.style.format({'EV（亿元）':'{:.2f}','EV变化(%)':'{:+.2f}'}),
             hide_index=True,use_container_width=True)
st.download_button('⬇️ 下载 Day 5.5 联合压力测试 CSV',
    stress_df55.to_csv(index=False).encode('utf-8-sig'),
    file_name='AlphaLens_Day5_5_Joint_Stress.csv',mime='text/csv',key='d55_stress_csv')
st.caption('© 2026 Frida AlphaLens AI · Day 5.5 Prototype · Fictional data only')


# Day 5.6 · Global Sensitivity & Risk Diagnostics
st.divider()
st.markdown("## Day 5.6 · Global Sensitivity & Risk Contribution | 全局敏感性与风险贡献")
st.caption("基于 Day 5.5 当前相关性模型的有效模拟样本；区分统计关联、模型敏感性与风险归因。以下不是因果识别，也不代表市场校准的真实概率。")

D56_NAMES = ["收入增长率", "FCF 率", "WACC", "永续增长率"]

def d56_diagnostics(x, y, names, baseline, seed=42):
    """Descriptive diagnostics on the conditional-on-valid joint distribution."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(y) & np.isfinite(x).all(axis=1)
    x, y = x[mask], y[mask]
    if len(y) < 100:
        raise ValueError("有效样本不足 100 个")
    sx = x.std(axis=0)
    sy = float(y.std())
    if sy <= 1e-12 or np.any(sx <= 1e-12):
        raise ValueError("至少一个输入或 EV 没有足够波动，无法进行标准化敏感性分析")
    zx = (x - x.mean(axis=0)) / sx
    zy = (y - y.mean()) / sy
    beta = np.linalg.lstsq(np.column_stack([np.ones(len(zx)), zx]), zy, rcond=None)[0][1:]
    predicted = zx @ beta
    r2 = float(max(0, 1 - np.sum((zy - predicted)**2) / np.sum(zy**2)))
    pearson = np.array([np.corrcoef(x[:, j], y)[0, 1] for j in range(x.shape[1])])
    # Spearman via average ranks, including ties.
    rank_y = pd.Series(y).rank(method="average").to_numpy()
    spearman = np.array([
        np.corrcoef(pd.Series(x[:, j]).rank(method="average").to_numpy(), rank_y)[0, 1]
        for j in range(x.shape[1])
    ])
    # Drop-column R2: incremental linear explanatory power conditional on other inputs.
    drop_r2 = []
    for j in range(x.shape[1]):
        z_reduced = np.delete(zx, j, axis=1)
        coef = np.linalg.lstsq(np.column_stack([np.ones(len(zx)), z_reduced]), zy, rcond=None)[0]
        fitted = coef[0] + z_reduced @ coef[1:]
        reduced_r2 = 1 - np.mean((zy - fitted)**2) / np.mean(zy**2)
        drop_r2.append(max(0.0, r2 - float(reduced_r2)))
    # Conditional sample correlations reflect both assumed correlation and validity filtering.
    out = pd.DataFrame({
        "驱动因素": names,
        "标准化回归系数": beta,
        "Pearson(EV)": pearson,
        "Spearman(EV)": spearman,
        "独有线性解释度增量": drop_r2,
    })
    return out, {"valid_draws": len(y), "linear_r2": r2,
                 "ev_std_100m_cny": sy, "baseline_ev_100m_cny": float(baseline),
                 "sample_input_correlation": np.corrcoef(x, rowvar=False).tolist()}

if "d55_cor" in globals() and isinstance(d55_cor, dict) and "draws" in d55_cor:
    try:
        d56_inputs = d55_cor["draws"][d55_cor["valid"]]
        d56_ev = d55_cor["good"]
        d56_table, d56_meta = d56_diagnostics(
            d56_inputs, d56_ev, D56_NAMES, float(baseline53))
        d56_sort = d56_table.reindex(
            d56_table["标准化回归系数"].abs().sort_values(ascending=False).index
        ).reset_index(drop=True)
        c56a, c56b, c56c = st.columns(3)
        c56a.metric("有效模拟情景", f'{d56_meta["valid_draws"]:,}')
        c56b.metric("线性模型样本内 R²", f'{d56_meta["linear_r2"]:.3f}')
        c56c.metric("EV 标准差", f'{d56_meta["ev_std_100m_cny"]:.2f} 亿元')
        st.markdown("### 估值敏感性排序")
        st.dataframe(d56_sort.style.format({
            "标准化回归系数": "{:+.3f}",
            "Pearson(EV)": "{:+.3f}",
            "Spearman(EV)": "{:+.3f}",
            "独有线性解释度增量": "{:.3f}",
        }), use_container_width=True, hide_index=True)
        fig56 = go.Figure(go.Bar(
            x=d56_sort["标准化回归系数"],
            y=d56_sort["驱动因素"],
            orientation="h",
            marker_color=["#62D2C4" if v >= 0 else "#E7868B"
                          for v in d56_sort["标准化回归系数"]]
        ))
        fig56.update_layout(
            title="标准化回归敏感性（正负方向保留）",
            xaxis_title="输入增加 1 个样本标准差对应的 EV 标准差变化（线性近似）",
            yaxis_title="", yaxis=dict(autorange="reversed"),
            template="plotly_dark", paper_bgcolor="#101C30",
            plot_bgcolor="#17263B", font=dict(color="#F5F8FC"),
            margin=dict(l=30, r=25, t=65, b=60), height=340
        )
        st.plotly_chart(fig56, use_container_width=True)
        st.info("标准化回归系数衡量控制其他输入后的线性敏感性；Pearson/Spearman 衡量单变量关联。由于输入相关、DCF 非线性和有效样本筛选，它们均不能直接当作各因素的独立方差贡献。")
        with st.expander("🔎 相关性与稳健性诊断", expanded=False):
            st.write("有效样本的实际相关性（可能因剔除无效情景而偏离设定值）：")
            st.dataframe(
                pd.DataFrame(d56_meta["sample_input_correlation"],
                             index=D56_NAMES, columns=D56_NAMES).style.format("{:.3f}"),
                use_container_width=True)
            st.write("独有线性解释度增量是移除该变量后，样本内线性 R² 的下降量；多个变量之间的共享解释度不会被分配，因此各项通常不加总为 R²。")
            if d56_meta["linear_r2"] < 0.8:
                st.warning("线性模型解释度有限：DCF 的非线性或交互作用可能很强，不宜仅依据回归系数排序做投资判断。")
            if d55_cor["valid_rate"] < .95:
                st.warning("有效率低于 95%：诊断仅针对有效情景的条件分布，可能存在筛选偏差。")
        d56_report = {
            "version": "Day 5.6",
            "fictional_data": True,
            "source": "Day 5.5 correlated valid Monte Carlo draws",
            "interpretation": "descriptive, conditional-on-valid; not causal or variance allocation",
            "metrics": d56_meta,
            "drivers": d56_table.to_dict(orient="records")
        }
        st.download_button("⬇️ 下载 Day 5.6 敏感性 CSV",
            d56_table.to_csv(index=False).encode("utf-8-sig"),
            file_name="AlphaLens_Day5_6_Sensitivity.csv",
            mime="text/csv", key="d56_csv")
        st.download_button("⬇️ 下载 Day 5.6 审计 JSON",
            json.dumps(d56_report, ensure_ascii=False, indent=2).encode("utf-8"),
            file_name="AlphaLens_Day5_6_Audit.json",
            mime="application/json", key="d56_json")
    except (ValueError, np.linalg.LinAlgError) as e:
        st.warning(f"Day 5.6 暂时无法计算：{e}")
else:
    st.warning("请先在 Day 5.5 设置有效的相关性矩阵并完成模拟。")

st.caption("© 2026 Frida AlphaLens AI · Day 5.6 Prototype · Fictional data only")



# === ALPHALENS DAY 5.7 ADDON ===
# Deterministic nonlinear response and interaction diagnostics, fictional data only.
import numpy as np

D57_NAMES = ['收入增长率', 'FCF 率', 'WACC', '永续增长率']
D57_KEYS = ['growth', 'margin', 'wacc', 'terminal_growth']

def d57_ev(params):
    g_, m_, w_, t_ = [float(v) for v in params]
    if not np.all(np.isfinite(params)) or g_ <= -1 or m_ < 0 or w_ <= 0 or t_ < 0 or w_ <= t_:
        return np.nan
    try:
        v = float(ev_for(g_, m_, w_, t_, float(base['revenue'])))
        return v if np.isfinite(v) else np.nan
    except (ValueError, OverflowError, ZeroDivisionError):
        return np.nan

def d57_pair_grid(center, i, j, range_i_pp, range_j_pp, count=21):
    offsets_i = np.linspace(-range_i_pp, range_i_pp, count) / 100
    offsets_j = np.linspace(-range_j_pp, range_j_pp, count) / 100
    z = np.full((count, count), np.nan)
    for row, dj in enumerate(offsets_j):
        for col, di in enumerate(offsets_i):
            p = center.copy()
            p[i] += di
            p[j] += dj
            z[row, col] = d57_ev(p)
    return offsets_i * 100, offsets_j * 100, z

def d57_interaction(center, i, j, di, dj):
    v00 = d57_ev(center)
    p10 = center.copy(); p10[i] += di
    p01 = center.copy(); p01[j] += dj
    p11 = center.copy(); p11[i] += di; p11[j] += dj
    v10, v01, v11 = d57_ev(p10), d57_ev(p01), d57_ev(p11)
    if not np.all(np.isfinite([v00, v10, v01, v11])):
        return None
    interaction = v11 - v10 - v01 + v00
    return {'base_ev': v00, 'i_only_ev': v10, 'j_only_ev': v01,
            'joint_ev': v11, 'interaction_ev': interaction,
            'joint_delta_ev': v11-v00, 'additive_delta_ev': v10+v01-2*v00,
            'reconciliation_error': (v11-v00)-((v10-v00)+(v01-v00)+interaction)}

st.divider()
st.markdown('## Day 5.7 · Nonlinear Sensitivity & Interaction Diagnostics | 非线性敏感性与交互效应诊断')
st.caption('基于现有简化 DCF 精确重估；分析数学响应，不是统计因果识别或市场校准的风险预测。全部公司数据均为虚构。')
center57 = np.array([growth, margin, wacc, terminal_growth], dtype=float)
base57 = d57_ev(center57)

with st.expander('⚙️ Day 5.7 分析设置', expanded=True):
    ca57, cb57 = st.columns(2)
    with ca57:
        i57 = st.selectbox('横轴变量', range(4), index=2, format_func=lambda x:D57_NAMES[x], key='d57_i')
        ri57 = st.slider('横轴变化范围（±百分点）', 0.5, 5.0, 2.0, 0.5, key='d57_ri')
    with cb57:
        choices57 = [j for j in range(4) if j != i57]
        j57 = st.selectbox('纵轴变量', choices57, index=choices57.index(3) if 3 in choices57 else 0,
                          format_func=lambda x:D57_NAMES[x], key='d57_j')
        rj57 = st.slider('纵轴变化范围（±百分点）', 0.5, 5.0, 1.0, 0.5, key='d57_rj')
    step57 = st.slider('交互效应冲击幅度（每个变量 +百分点）', 0.1, 2.0, 0.5, 0.1, key='d57_step')

xs57, ys57, z57 = d57_pair_grid(center57, i57, j57, ri57, rj57)
valid57 = np.isfinite(z57)
mc57a, mc57b, mc57c = st.columns(3)
mc57a.metric('基准 EV', f'{base57:.2f} 亿元')
mc57b.metric('网格有效率', f'{valid57.mean():.1%}')
mc57c.metric('网格有效情景', f'{valid57.sum():,} / {z57.size:,}')
if not valid57.all():
    st.warning('部分网格情景不满足 DCF 约束（如 WACC ≤ 永续增长率）；这些格子不参与结果。')

st.markdown('### 二维非线性估值响应热力图')
fig57 = go.Figure(go.Heatmap(x=xs57, y=ys57, z=z57,
    colorscale=[[0, '#25456B'], [0.5, '#357D94'], [1, '#6CD9CB']],
    colorbar=dict(title='EV（亿元）'),
    hovertemplate=f'{D57_NAMES[i57]} 冲击 %{{x:+.2f}}pp<br>{D57_NAMES[j57]} 冲击 %{{y:+.2f}}pp<br>EV %{{z:.2f}} 亿元<extra></extra>'))
fig57.add_trace(go.Scatter(x=[0], y=[0], mode='markers', name='基准',
    marker=dict(color='#F5F8FC', size=11, symbol='x', line=dict(width=2))))
fig57.update_layout(title='双因素精确重估（相对当前基准的百分点冲击）',
    xaxis_title=f'{D57_NAMES[i57]}（pp）', yaxis_title=f'{D57_NAMES[j57]}（pp）',
    paper_bgcolor='#101C30', plot_bgcolor='#17263B', font=dict(color='#F5F8FC'), height=490)
st.plotly_chart(fig57, use_container_width=True)

st.markdown('### 单因素响应曲线：观察斜率与曲率')
curve57 = []
figcurve57 = go.Figure()
for idx57, range57 in [(i57,ri57),(j57,rj57)]:
    xx57 = np.linspace(-range57, range57, 61)
    yy57 = []
    for delta57 in xx57:
        p57 = center57.copy(); p57[idx57] += delta57/100
        yy57.append(d57_ev(p57))
        curve57.append({'variable':D57_NAMES[idx57], 'shock_pp':float(delta57), 'ev_100m_cny':float(yy57[-1])})
    figcurve57.add_trace(go.Scatter(x=xx57, y=yy57, mode='lines', name=D57_NAMES[idx57]))
figcurve57.add_hline(y=base57, line_dash='dash', line_color='#A9BCD1')
figcurve57.update_layout(xaxis_title='单因素冲击（百分点）', yaxis_title='EV（亿元）',
    paper_bgcolor='#101C30', plot_bgcolor='#17263B', font=dict(color='#F5F8FC'), height=390)
st.plotly_chart(figcurve57, use_container_width=True)
st.caption('两条曲线均固定其余三个参数。斜率变化代表局部敏感性变化；在 WACC 接近永续增长率时，终值可能急剧上升。')

st.markdown('### 双因素交互效应：精确有限差分')
inter57 = d57_interaction(center57, i57, j57, step57/100, step57/100)
if inter57 is None:
    st.warning('当前正向联合冲击包含无效估值情景，请调整变量或冲击幅度。')
else:
    ia57, ib57, ic57 = st.columns(3)
    ia57.metric('联合 EV 变化', f'{inter57["joint_delta_ev"]:+.3f} 亿元')
    ib57.metric('单因素变化之和', f'{inter57["additive_delta_ev"]:+.3f} 亿元')
    ic57.metric('额外交互项', f'{inter57["interaction_ev"]:+.3f} 亿元')
    st.latex(r'I_{ij}=EV(x+\Delta_i+\Delta_j)-EV(x+\Delta_i)-EV(x+\Delta_j)+EV(x)')
    st.write('正值表示本次联合冲击的 EV 变化高于两项单独变化之和；负值表示低于该加总。符号不直接等同于风险放大或风险缓释，需结合冲击方向判断。')
    st.success('交互分解闭合校验通过。' if abs(inter57['reconciliation_error']) < 1e-7 else '交互分解未闭合。')

st.markdown('### 局部敏感性 vs Day 5.6 全局线性敏感性')
local57 = []
for k57 in range(4):
    h57 = 0.001  # 0.1 percentage point, in decimal parameter units
    pa57=center57.copy(); pb57=center57.copy()
    pa57[k57]+=h57; pb57[k57]-=h57
    va57=d57_ev(pa57); vb57=d57_ev(pb57)
    slope57=(va57-vb57)/0.2 if np.isfinite(va57) and np.isfinite(vb57) else np.nan
    local57.append({'驱动因素':D57_NAMES[k57], '局部斜率（亿元/pp）':slope57})
local_df57 = pd.DataFrame(local57)
if 'd56_table' in globals() and isinstance(d56_table, pd.DataFrame):
    local_df57 = local_df57.merge(d56_table[['驱动因素','标准化回归系数']], on='驱动因素', how='left')
st.dataframe(local_df57.style.format({'局部斜率（亿元/pp）':'{:+.3f}',
    **({'标准化回归系数':'{:+.3f}'} if '标准化回归系数' in local_df57 else {})}),
    hide_index=True, use_container_width=True)
st.info('局部斜率的单位为亿元/百分点；Day 5.6 标准化系数为标准差/标准差，两者量纲不同，不能直接比较数值大小。')

report57 = {'version':'Day 5.7', 'fictional_data':True, 'company':company,
    'base_parameters':dict(zip(D57_KEYS, center57.tolist())), 'base_ev_100m_cny':base57,
    'axes':[D57_NAMES[i57],D57_NAMES[j57]], 'ranges_pp':[ri57,rj57],
    'grid_valid_rate':float(valid57.mean()), 'grid_ev_100m_cny':[[None if not np.isfinite(v) else float(v) for v in row] for row in z57],
    'grid_x_shock_pp':xs57.tolist(), 'grid_y_shock_pp':ys57.tolist(),
    'interaction_shock_pp':step57, 'interaction':inter57,
    'local_sensitivity':local_df57.replace({np.nan:None}).to_dict(orient='records'),
    'limitations':'Mathematical model sensitivity only; not causal, market calibrated, or a probability forecast.'}
st.download_button('⬇️ 下载 Day 5.7 响应曲线 CSV',
    pd.DataFrame(curve57).to_csv(index=False).encode('utf-8-sig'),
    file_name='AlphaLens_Day5_7_Response_Curves.csv', mime='text/csv', key='d57_curve_csv')
st.download_button('⬇️ 下载 Day 5.7 审计 JSON',
    json.dumps(report57, ensure_ascii=False, indent=2, allow_nan=False).encode('utf-8'),
    file_name='AlphaLens_Day5_7_Audit.json', mime='application/json', key='d57_audit_json')
st.caption('© 2026 Frida AlphaLens AI · Day 5.7 Prototype · Fictional data only')


# === ALPHALENS DAY 5.8 ADDON ===
# Exact scenario repricing, Shapley decomposition, threshold vulnerability.
# All inputs fictional; no inferred likelihoods or causal effects.
import itertools as _it58
import math as _math58

st.divider()
st.markdown('## Day 5.8 · Scenario Risk Decomposition & Decision Intelligence | 情景风险分解与决策支持')
st.caption('复用 Day 5.7 的原始 DCF 函数；情景冲击、阈值及结果均为假设分析，不代表发生概率、真实市场风险或投资建议。')

_center58 = np.array([growth, margin, wacc, terminal_growth], dtype=float)
_base58 = d57_ev(_center58)
_names58 = D57_NAMES

with st.expander('⚙️ Day 5.8 情景与阈值设置', expanded=True):
    _mode58 = st.selectbox('情景模板', ['自定义冲击', '悲观：增长与现金流下降、WACC 上升', '乐观：增长与现金流上升、WACC 下降'], key='d58_mode')
    _presets58 = {
        '自定义冲击': (-2.0, -1.0, 1.0, 0.0),
        '悲观：增长与现金流下降、WACC 上升': (-3.0, -2.0, 1.0, -0.5),
        '乐观：增长与现金流上升、WACC 下降': (3.0, 2.0, -1.0, 0.5),
    }
    _default58 = _presets58[_mode58]
    _cols58 = st.columns(4)
    _shock58 = np.array([
        _cols58[k].number_input(f'{_names58[k]}冲击 (pp)', min_value=-20.0 if k < 2 else -10.0,
            max_value=20.0 if k < 2 else 10.0, value=float(_default58[k]), step=0.5,
            key=f'd58_shock_{_mode58}_{k}')
        for k in range(4)
    ], dtype=float)
    _threshold58 = st.slider('脆弱性阈值：基准 EV 的百分比', 40, 120, 80, 5, key='d58_threshold')
    _range58 = st.slider('二维压力网格：各变量 ±百分点', 0.5, 5.0, 2.0, 0.5, key='d58_grid_range')
    _axiscols58 = st.columns(2)
    _x58 = _axiscols58[0].selectbox('压力网格横轴', range(4), index=2, format_func=lambda i:_names58[i], key='d58_x')
    _yoptions58 = [i for i in range(4) if i != _x58]
    _y58 = _axiscols58[1].selectbox('压力网格纵轴', _yoptions58, index=_yoptions58.index(1) if 1 in _yoptions58 else 0,
                                    format_func=lambda i:_names58[i], key='d58_y')

_target58 = _center58 + _shock58 / 100.0
_ev58 = d57_ev(_target58)
if not np.isfinite(_base58) or not np.isfinite(_ev58):
    st.error('基准或冲击后参数违反 DCF 有效性约束。请调整 WACC、永续增长率或其他冲击。')
else:
    _threshold_ev58 = _base58 * _threshold58 / 100
    _metriccols58 = st.columns(4)
    _metriccols58[0].metric('基准 EV', f'{_base58:,.2f} 亿元')
    _metriccols58[1].metric('情景 EV', f'{_ev58:,.2f} 亿元')
    _metriccols58[2].metric('情景估值变化', f'{_ev58-_base58:+,.2f} 亿元', f'{(_ev58/_base58-1)*100:+.2f}%')
    _metriccols58[3].metric('阈值 EV', f'{_threshold_ev58:,.2f} 亿元')

    st.markdown('### 1. 精确 Shapley 情景归因（四因素）')
    _subset58 = {}
    for _mask58 in range(16):
        _p58 = np.array([_target58[i] if _mask58 & (1 << i) else _center58[i] for i in range(4)])
        _subset58[_mask58] = d57_ev(_p58)
    _valid_subset58 = all(np.isfinite(v) for v in _subset58.values())
    _shapley58 = None
    if not _valid_subset58:
        st.warning('16 个混合情景中存在无效 DCF 输入，无法计算完整 Shapley 归因；请缩小冲击。')
    else:
        _contrib58 = np.zeros(4)
        for _order58 in _it58.permutations(range(4)):
            _mask58 = 0
            for _idx58 in _order58:
                _next58 = _mask58 | (1 << _idx58)
                _contrib58[_idx58] += (_subset58[_next58] - _subset58[_mask58]) / 24.0
                _mask58 = _next58
        _shapley58 = _contrib58
        _resid58 = float((_ev58 - _base58) - _contrib58.sum())
        _attr58 = pd.DataFrame({'驱动因素':_names58, '冲击（pp）':_shock58,
                                'Shapley EV 贡献（亿元）':_contrib58,
                                '占基准 EV（%）':_contrib58/_base58*100})
        st.dataframe(_attr58.style.format({'冲击（pp）':'{:+.2f}', 'Shapley EV 贡献（亿元）':'{:+.3f}',
                                          '占基准 EV（%）':'{:+.2f}'}), hide_index=True, use_container_width=True)
        _fig58 = go.Figure(go.Bar(x=_names58, y=_contrib58,
            marker_color=[TEAL if v >= 0 else RED for v in _contrib58],
            text=[f'{v:+.2f}' for v in _contrib58], textposition='outside'))
        _fig58.update_layout(yaxis_title='EV 贡献（亿元）')
        st.plotly_chart(format_plot(_fig58, '情景估值变化的 Shapley 分解', 390), use_container_width=True)
        if abs(_resid58) <= 1e-8*max(1,abs(_ev58)):
            st.success(f'16 个混合情景、24 种变量顺序归因闭合：残差 {_resid58:.3e} 亿元。')
        else:
            st.error(f'归因闭合失败：残差 {_resid58:.3e} 亿元。')
        st.caption('Shapley 是模型内分摊规则，不是统计因果贡献，也不是各风险的发生概率。')

    st.markdown('### 2. 情景脆弱性与阈值诊断')
    _xs58, _ys58, _grid58 = d57_pair_grid(_center58, _x58, _y58, _range58, _range58, count=31)
    _valid58 = np.isfinite(_grid58)
    _breach58 = _valid58 & (_grid58 < _threshold_ev58)
    _count58 = int(_valid58.sum())
    _breach_count58 = int(_breach58.sum())
    _gridcols58 = st.columns(3)
    _gridcols58[0].metric('有效网格情景', f'{_count58:,} / {_grid58.size:,}')
    _gridcols58[1].metric('低于阈值的网格点', f'{_breach_count58:,}')
    _gridcols58[2].metric('有效网格中阈值触发占比', f'{_breach_count58/_count58:.1%}' if _count58 else 'N/A')
    _figgrid58 = go.Figure(go.Heatmap(x=_xs58, y=_ys58, z=_grid58,
        colorscale=[[0,'#25456B'],[0.5,'#357D94'],[1,TEAL]],
        colorbar=dict(title='EV（亿元）'),
        hovertemplate=f'{_names58[_x58]} %{{x:+.2f}}pp<br>{_names58[_y58]} %{{y:+.2f}}pp<br>EV %{{z:.2f}}亿元<extra></extra>'))
    if _count58 and np.nanmin(_grid58) <= _threshold_ev58 <= np.nanmax(_grid58):
        _figgrid58.add_trace(go.Contour(x=_xs58,y=_ys58,z=_grid58,
            contours=dict(start=_threshold_ev58,end=_threshold_ev58,size=1,coloring='lines',showlabels=True),
            line=dict(color='#F5F8FC',width=3), showscale=False, name='阈值边界',
            hoverinfo='skip'))
    _figgrid58.add_trace(go.Scatter(x=[0],y=[0],mode='markers',name='基准',
        marker=dict(symbol='x',size=12,color='#F5F8FC')))
    _figgrid58.update_layout(xaxis_title=f'{_names58[_x58]}冲击 (pp)',
        yaxis_title=f'{_names58[_y58]}冲击 (pp)', showlegend=True)
    st.plotly_chart(format_plot(_figgrid58, '双因素压力测试与阈值边界', 500), use_container_width=True)
    st.info('网格触发占比只是均匀取点的数学比例，不是违约概率、损失概率或 VaR。其大小依赖变量范围、步长和固定的其他假设。')

    st.markdown('### 3. 决策支持摘要 · 规则生成')
    _status58 = '低于' if _ev58 < _threshold_ev58 else '不低于'
    _summary58 = [f'当前虚构公司的基准 EV 为 {_base58:.2f} 亿元，指定情景 EV 为 {_ev58:.2f} 亿元，变化 {(_ev58/_base58-1)*100:+.2f}%。',
        f'该情景 EV {_status58}预设阈值（基准 EV 的 {_threshold58}%，即 {_threshold_ev58:.2f} 亿元）。',
        f'二维压力网格中，{_breach_count58}/{_count58} 个有效点低于阈值；此比例不能解释为事件发生概率。']
    if _shapley58 is not None:
        _rank58 = sorted(range(4),key=lambda i:abs(_shapley58[i]),reverse=True)
        _summary58.append(f'按 Shapley 绝对估值贡献，主要模型驱动因素为 {_names58[_rank58[0]]}（{_shapley58[_rank58[0]]:+.2f} 亿元）；这是给定冲击下的归因，不代表真实风险排序。')
    _summary58.append('下一步应验证冲击假设的经济依据、终值占比、财务数据来源及行业可比估值；本模型未校准市场分布。')
    st.write('\n\n'.join(_summary58))

    _gridrows58 = [{'x_shock_pp':float(x), 'y_shock_pp':float(y),
                    'ev_100m_cny':float(_grid58[j,i]) if np.isfinite(_grid58[j,i]) else None,
                    'valid':bool(_valid58[j,i]),'below_threshold':bool(_breach58[j,i])}
                    for j,y in enumerate(_ys58) for i,x in enumerate(_xs58)]
    _audit58 = {'version':'Day 5.8','fictional_data':True,'company':company,
        'method':'exact_dcf_shapley_24_orders_and_deterministic_grid',
        'currency_unit':'CNY 100 million',
        'baseline_parameters':dict(zip(D57_KEYS,map(float,_center58))),
        'shock_pp':dict(zip(D57_KEYS,map(float,_shock58))),
        'scenario_parameters':dict(zip(D57_KEYS,map(float,_target58))),
        'baseline_ev':float(_base58),'scenario_ev':float(_ev58),
        'scenario_delta_ev':float(_ev58-_base58),
        'threshold_pct_of_base':_threshold58,'threshold_ev':float(_threshold_ev58),
        'shapley_contributions':None if _shapley58 is None else dict(zip(D57_KEYS,map(float,_shapley58))),
        'shapley_reconciliation_error':None if _shapley58 is None else _resid58,
        'all_16_subsets_valid':bool(_valid_subset58),
        'grid_axes':[_names58[_x58],_names58[_y58]],'grid_range_pp':_range58,
        'grid_valid_count':_count58,'grid_breach_count':_breach_count58,
        'grid_breach_fraction_not_probability':_breach_count58/_count58 if _count58 else None,
        'summary':_summary58,
        'limitations':'Fictional data; mathematical stress test only. No causal attribution or market-calibrated probabilities.'}
    _export58a, _export58b = st.columns(2)
    _export58a.download_button('⬇️ 下载 Day 5.8 网格 CSV',
        pd.DataFrame(_gridrows58).to_csv(index=False).encode('utf-8-sig'),
        file_name='AlphaLens_Day5_8_Stress_Grid.csv',mime='text/csv',key='d58_csv')
    _export58b.download_button('⬇️ 下载 Day 5.8 审计 JSON',
        json.dumps(_audit58,ensure_ascii=False,indent=2,allow_nan=False).encode('utf-8'),
        file_name='AlphaLens_Day5_8_Audit.json',mime='application/json',key='d58_json')
    st.caption('© 2026 Frida AlphaLens AI · Day 5.8 Prototype · Fictional data only')

# === ALPHALENS DAY 5.9: REVERSE STRESS TESTING ===
# Deterministic fictional-data diagnostics; preserves the original DCF engine.
st.divider()
st.markdown('## Day 5.9 · Reverse Stress Testing & Valuation Resilience | 反向压力测试与估值韧性')
st.caption('反向求解估值跌破阈值所需冲击；不代表冲击概率、真实市场预测或投资建议。')
_d59_center = np.array([growth, margin, wacc, terminal_growth], dtype=float)
_d59_base = d57_ev(_d59_center)
with st.expander('⚙️ Day 5.9 反向压力设置', expanded=True):
    _d59_threshold = st.slider('目标 EV（基准 EV 百分比）', 40, 100, 80, 5, key='d59_threshold')
    _d59_max = st.slider('单因素最大搜索冲击（百分点）', 1.0, 20.0, 10.0, 0.5, key='d59_max')
    _d59_cols = st.columns(2)
    _d59_x = _d59_cols[0].selectbox('联合冲击横轴', range(4), index=2, format_func=lambda i:D57_NAMES[i], key='d59_x')
    _d59_yopts = [i for i in range(4) if i != _d59_x]
    _d59_y = _d59_cols[1].selectbox('联合冲击纵轴', _d59_yopts, index=_d59_yopts.index(1) if 1 in _d59_yopts else 0, format_func=lambda i:D57_NAMES[i], key='d59_y')
    _d59_gridrange = st.slider('联合冲击绘图范围（各轴 ±pp）', 1.0, 10.0, 4.0, 0.5, key='d59_gridrange')
_d59_target = _d59_base * _d59_threshold / 100 if np.isfinite(_d59_base) else np.nan

def d59_evaluate(offsets_pp):
    return d57_ev(_d59_center + np.asarray(offsets_pp, dtype=float)/100.0)

def d59_root(direction_pp, max_scale=1.0, n_scan=240):
    """First downward threshold crossing along a specified shock ray; no monotonicity assumed."""
    prev_s, prev_v = 0.0, d59_evaluate(np.zeros(4))
    if not np.isfinite(prev_v):
        return None, 'invalid baseline'
    for s in np.linspace(max_scale/n_scan, max_scale, n_scan):
        v = d59_evaluate(direction_pp*s)
        if not np.isfinite(v):
            return None, 'invalid DCF before threshold crossing'
        if v <= _d59_target and prev_v > _d59_target:
            lo, hi = prev_s, float(s)
            for _ in range(65):
                mid = (lo+hi)/2
                vm = d59_evaluate(direction_pp*mid)
                if not np.isfinite(vm):
                    return None, 'invalid DCF during bisection'
                if vm <= _d59_target: hi = mid
                else: lo = mid
            return hi, 'solved'
        prev_s, prev_v = float(s), v
    return None, 'no crossing in searched range'

if not np.isfinite(_d59_base) or _d59_base <= 0:
    st.error('当前基准 EV 无效或非正，无法按基准百分比执行反向压力测试。')
else:
    _d59_kpis = st.columns(3)
    _d59_kpis[0].metric('基准 EV', f'{_d59_base:,.2f} 亿元')
    _d59_kpis[1].metric('阈值 EV', f'{_d59_target:,.2f} 亿元')
    _d59_kpis[2].metric('估值缓冲', f'{_d59_base-_d59_target:,.2f} 亿元')
    st.markdown('### 1. 单因素临界冲击｜最先触发阈值的方向')
    _d59_signs = [-1,-1,1,-1]
    _d59_rows=[]
    for idx in range(4):
        ray = np.zeros(4); ray[idx]=_d59_signs[idx]*_d59_max
        scale,status = d59_root(ray)
        shock = float(ray[idx]*scale) if scale is not None else None
        actual = d59_evaluate(ray*scale) if scale is not None else None
        _d59_rows.append({'驱动因素':D57_NAMES[idx], '不利冲击方向':'下降' if _d59_signs[idx]<0 else '上升',
            '临界冲击 (pp)':shock, '临界参数值 (%)':float((_d59_center[idx]+shock/100)*100) if shock is not None else None,
            '重新定价 EV (亿元)':actual, '求解状态':status})
    st.dataframe(pd.DataFrame(_d59_rows), use_container_width=True, hide_index=True)
    st.caption('在每个因素的指定不利方向上，从基准逐步扫描并二分求解首个阈值交点。无解不表示现实中不存在风险。')
    st.markdown('### 2. 双因素反向压力边界')
    _d59_xs=np.linspace(-_d59_gridrange,_d59_gridrange,61)
    _d59_ys=np.linspace(-_d59_gridrange,_d59_gridrange,61)
    _d59_z=np.full((61,61),np.nan)
    for iy,dy in enumerate(_d59_ys):
        for ix,dx in enumerate(_d59_xs):
            offsets=np.zeros(4);offsets[_d59_x]=dx;offsets[_d59_y]=dy
            _d59_z[iy,ix]=d59_evaluate(offsets)
    _d59_valid=np.isfinite(_d59_z)
    _d59_breach=_d59_valid & (_d59_z<_d59_target)
    import plotly.graph_objects as _go59
    _d59_fig=_go59.Figure()
    _d59_fig.add_trace(_go59.Heatmap(x=_d59_xs,y=_d59_ys,z=_d59_z,colorscale='Teal',colorbar=dict(title='EV (亿元)'),hovertemplate='X %{x:.2f}pp<br>Y %{y:.2f}pp<br>EV %{z:.2f}亿元<extra></extra>'))
    if np.any(_d59_valid & (_d59_z<_d59_target)) and np.any(_d59_valid & (_d59_z>=_d59_target)):
        _d59_fig.add_trace(_go59.Contour(x=_d59_xs,y=_d59_ys,z=_d59_z,contours=dict(start=_d59_target,end=_d59_target,size=1,coloring='none'),line=dict(color='#ffce73',width=3),showscale=False,name='估值阈值边界',hoverinfo='skip'))
    _d59_fig.add_trace(_go59.Scatter(x=[0],y=[0],mode='markers',marker=dict(symbol='x',size=13,color='white'),name='基准点'))
    _d59_fig.update_layout(template='plotly_dark',paper_bgcolor='#0e1b30',plot_bgcolor='#17283f',height=530,xaxis_title=f'{D57_NAMES[_d59_x]}冲击 (pp)',yaxis_title=f'{D57_NAMES[_d59_y]}冲击 (pp)',margin=dict(l=35,r=35,t=25,b=45))
    st.plotly_chart(_d59_fig,use_container_width=True)
    st.write(f'有效网格点 **{int(_d59_valid.sum())}/{_d59_valid.size}**；低于阈值的有效网格点 **{int(_d59_breach.sum())}**。该占比不是概率。')
    st.markdown('### 3. 最小标准化联合冲击｜限定为两个选定因素')
    st.caption('采用二维不利方向射线搜索，寻找欧氏标准化幅度最小的阈值交点；这是离散方向近似，不是全局最优性证明。')
    _d59_best=None
    for theta in np.linspace(0,np.pi/2,181):
        direction=np.zeros(4)
        direction[_d59_x]=_d59_signs[_d59_x]*np.cos(theta)*_d59_max
        direction[_d59_y]=_d59_signs[_d59_y]*np.sin(theta)*_d59_max
        scale,status=d59_root(direction,n_scan=100)
        if scale is not None:
            offsets=direction*scale
            norm=float(np.linalg.norm(offsets))
            if _d59_best is None or norm<_d59_best['norm']:
                _d59_best={'norm':norm,'offsets':offsets,'ev':d59_evaluate(offsets)}
    if _d59_best is None:
        st.warning('当前搜索范围内未找到有效的二维不利冲击阈值交点。可扩大搜索范围或切换因素。')
    else:
        st.metric('最小联合冲击幅度（二维欧氏 pp）',f"{_d59_best['norm']:.3f}")
        st.write(f"{D57_NAMES[_d59_x]} **{_d59_best['offsets'][_d59_x]:+.3f} pp**；{D57_NAMES[_d59_y]} **{_d59_best['offsets'][_d59_y]:+.3f} pp**；重新定价 EV **{_d59_best['ev']:.4f} 亿元**。")
    _d59_audit={'version':'Day 5.9','fictional_data':True,'baseline_parameters':dict(zip(D57_KEYS,map(float,_d59_center))),
        'baseline_ev':float(_d59_base),'threshold_pct':int(_d59_threshold),'threshold_ev':float(_d59_target),
        'single_factor_results':_d59_rows,'grid_axes':[D57_KEYS[_d59_x],D57_KEYS[_d59_y]],'grid_range_pp':float(_d59_gridrange),
        'grid_valid_count':int(_d59_valid.sum()),'grid_breach_count':int(_d59_breach.sum()),
        'joint_shock':None if _d59_best is None else {'shock_pp':dict(zip(D57_KEYS,map(float,_d59_best['offsets']))),'euclidean_pp':_d59_best['norm'],'revalued_ev':float(_d59_best['ev'])},
        'limitations':'Fictional inputs. No market calibration, event probability, or global optimum guarantee.'}
    _d59_export1,_d59_export2=st.columns(2)
    _d59_export1.download_button('⬇️ 下载 Day 5.9 临界冲击 CSV',pd.DataFrame(_d59_rows).to_csv(index=False).encode('utf-8-sig'),file_name='AlphaLens_Day5_9_Critical_Shocks.csv',mime='text/csv',key='d59_csv')
    _d59_export2.download_button('⬇️ 下载 Day 5.9 审计 JSON',json.dumps(_d59_audit,ensure_ascii=False,indent=2,allow_nan=False).encode('utf-8'),file_name='AlphaLens_Day5_9_Audit.json',mime='application/json',key='d59_json')
    st.caption('© 2026 Frida AlphaLens AI · Day 5.9 Prototype · Fictional data only')


# === ALPHALENS DAY 5.10: MODEL VALIDATION & AUDIT ===
st.divider()
st.markdown('## Day 5.10 · Model Validation & Audit | 模型验证与审计')
st.caption('独立于图表的确定性校验；仅验证内部数值一致性，不等于市场校准或模型外部验证。')
import hashlib as _hash510
from datetime import datetime as _datetime510, timezone as _timezone510

def d510_validate(center, target_pct=80, max_pp=10., seed=42):
    center=np.asarray(center,dtype=float)
    results=[]
    def record(name, ok, detail, metric=None):
        results.append({'检查项目':name,'结果':'PASS' if ok else 'FAIL','诊断':str(detail),'指标':metric})
    v=d57_ev(center)
    record('基准 DCF 可行性',bool(np.isfinite(v) and v>0),f'EV={v:.8f}' if np.isfinite(v) else '基准 EV 无效',float(v) if np.isfinite(v) else None)
    if not np.isfinite(v) or v<=0: return results,{}
    # Independent reference via the original DCF function and explicit cash-flow identity.
    direct=calculate_dcf(float(base['revenue']),*map(float,center))
    cf_identity=sum(direct['pv_fcfs'])+direct['pv_terminal']
    err=abs(v-cf_identity)
    record('DCF 现金流折现恒等式',err<=1e-8*max(1,abs(v)),f'绝对残差={err:.3e} 亿元',err)
    # Invalid financial domain should be rejected rather than silently valued.
    invalids=[('WACC ≤ g',np.array([center[0],center[1],center[3],center[3]])),
              ('FCF 率 < 0',np.array([center[0],-0.01,center[2],center[3]])),
              ('收入增长率 ≤ -100%',np.array([-1.,center[1],center[2],center[3]])),
              ('负永续增长率（当前模块约束）',np.array([center[0],center[1],center[2],-0.01]))]
    for name,params in invalids:
        ok=not np.isfinite(d57_ev(params))
        record('非法输入拒绝：'+name,ok,'正确拒绝' if ok else '错误地接受了非法输入')
    # Local economic monotonicity, using small finite shocks and feasible domain.
    signs=[1,1,-1,1]
    for i,name in enumerate(D57_NAMES):
        test=center.copy();test[i]+=0.0001
        vv=d57_ev(test)
        ok=np.isfinite(vv) and signs[i]*(vv-v)>0
        record('局部方向检查：'+name,bool(ok),f'增加 1bp 后 EV={vv:.6f}' if np.isfinite(vv) else '扰动后 DCF 无效',float(vv-v) if np.isfinite(vv) else None)
    # Independent threshold crossing bisection; do not depend on Day 5.9 closure/global state.
    target=v*target_pct/100.
    roots={}
    for i,name in enumerate(D57_NAMES):
        sign=[-1,-1,1,-1][i]
        lo=0.; hi=None
        for pp in np.linspace(0,max_pp,401)[1:]:
            test=center.copy();test[i]+=sign*pp/100
            vv=d57_ev(test)
            if not np.isfinite(vv):break
            if vv<=target:hi=float(pp);break
            lo=float(pp)
        if hi is None:
            roots[name]={'status':'not_found_in_feasible_search','shock_pp':None,'reprice_ev':None}
            record('反向求解：'+name,True,'未发现可行阈值交点（信息性状态，不视为求解成功）')
            continue
        for _ in range(55):
            mid=(lo+hi)/2
            test=center.copy();test[i]+=sign*mid/100
            if d57_ev(test)<=target:hi=mid
            else:lo=mid
        test=center.copy();test[i]+=sign*hi/100
        repriced=d57_ev(test)
        residual=abs(repriced-target)
        roots[name]={'status':'solved','shock_pp':float(sign*hi),'reprice_ev':float(repriced)}
        record('反向求解重定价：'+name,bool(residual<=1e-6*max(1,target)),f'临界冲击={sign*hi:+.6f}pp；残差={residual:.3e}亿元',float(residual))
    # Fixed seed reproducibility: same input noise, same output; different seed should alter draws.
    rng1=np.random.default_rng(int(seed));rng2=np.random.default_rng(int(seed));rng3=np.random.default_rng(int(seed)+1)
    a=rng1.standard_normal((1000,4));b=rng2.standard_normal((1000,4));c=rng3.standard_normal((1000,4))
    record('随机种子可复现性',bool(np.array_equal(a,b) and not np.array_equal(a,c)),'相同种子逐元素一致；不同种子抽样不同')
    # Finite perturbation sensitivity against 1bp shocks, no regression/causality interpretation.
    deltas=[]
    for i in range(4):
        test=center.copy();test[i]+=0.0001
        vi=d57_ev(test)
        deltas.append(float(vi-v) if np.isfinite(vi) else None)
    meta={'baseline_ev':float(v),'target_ev':float(target),'roots':roots,'one_bp_ev_deltas':dict(zip(D57_KEYS,deltas)),
          'model_domain':'growth>-100%; margin>=0; WACC>g>=0; WACC>0',
          'validation_scope':'Deterministic internal numerical checks only; not market calibration or independent external validation.'}
    return results,meta

with st.expander('⚙️ Day 5.10 验证参数',expanded=True):
    _d510_threshold=st.slider('验证用目标 EV（基准百分比）',40,100,80,5,key='d510_threshold')
    _d510_max=st.slider('验证搜索范围（pp）',1.,20.,10.,0.5,key='d510_max')
    _d510_seed=st.number_input('可复现性测试随机种子',min_value=0,max_value=1000000,value=42,step=1,key='d510_seed')
_d510_checks,_d510_meta=d510_validate(np.array([growth,margin,wacc,terminal_growth],dtype=float),_d510_threshold,_d510_max,int(_d510_seed))
_d510_df=pd.DataFrame(_d510_checks)
_d510_pass=sum(x['结果']=='PASS' for x in _d510_checks)
_d510_fail=len(_d510_checks)-_d510_pass
_d510_cols=st.columns(3)
_d510_cols[0].metric('通过检查',f'{_d510_pass}/{len(_d510_checks)}')
_d510_cols[1].metric('失败检查',str(_d510_fail))
_d510_cols[2].metric('模型验证状态','PASS' if _d510_fail==0 else 'REVIEW')
st.dataframe(_d510_df,use_container_width=True,hide_index=True)
if _d510_fail:st.error('存在未通过检查：请勿将该次运行标记为已验证。')
else:st.success('当前已执行的内部数值检查全部通过；不代表预测有效性或市场校准。')
st.markdown('### 反向求解审计与未解决事项')
st.dataframe(pd.DataFrame([{'因素':k,**val} for k,val in _d510_meta.get('roots',{}).items()]),use_container_width=True,hide_index=True)
st.info('永续增长率单因素搜索可能在 g=0 的模型约束处结束，仍未达到目标 EV；应标记为“可行范围内未触发”，而非误报为求解失败。当前只做内部一致性测试；Monte Carlo 的统计收敛、相关矩阵、Shapley 及真实数据准确性需要独立数据级测试。')
_d510_payload={'version':'Day 5.10','timestamp_utc':_datetime510.now(_timezone510.utc).isoformat(),
 'fictional_data':True,'inputs':{'growth':float(growth),'margin':float(margin),'wacc':float(wacc),'terminal_growth':float(terminal_growth),'revenue':float(base['revenue']),'threshold_pct':int(_d510_threshold),'search_max_pp':float(_d510_max),'seed':int(_d510_seed)},
 'checks':_d510_checks,'metadata':_d510_meta,'pass_count':_d510_pass,'fail_count':_d510_fail}
_d510_bytes=json.dumps(_d510_payload,ensure_ascii=False,indent=2,allow_nan=False).encode('utf-8')
_d510_digest=_hash510.sha256(_d510_bytes).hexdigest()
st.caption('审计 JSON SHA-256: '+_d510_digest)
_d510_a,_d510_b=st.columns(2)
_d510_a.download_button('⬇️ 下载 Day 5.10 验证报告 CSV',_d510_df.to_csv(index=False).encode('utf-8-sig'),file_name='AlphaLens_Day5_10_Validation.csv',mime='text/csv',key='d510_csv')
_d510_b.download_button('⬇️ 下载 Day 5.10 审计 JSON',_d510_bytes,file_name='AlphaLens_Day5_10_Audit.json',mime='application/json',key='d510_json')
st.caption('© 2026 Frida AlphaLens AI · Day 5.10 Prototype · Fictional data only')


# ================= DAY 6.1: HISTORICAL FINANCIAL DATA FOUNDATION =================
import io as _io61
import hashlib as _hash61
import json as _json61
from datetime import datetime as _dt61, timezone as _tz61

st.divider()
st.markdown('# Day 6.1 · Financial Data Foundation | 真实财务数据基础')
st.caption('Historical company data intake, validation and provenance. Data is user-provided and is NOT automatically market-verified. Day 5 fictional assumptions remain unchanged.')

_D61_FIELDS = {
 'revenue':'Revenue / 营业收入', 'cogs':'Cost of goods sold / 营业成本',
 'operating_income':'Operating income / 营业利润', 'net_income':'Net income / 净利润',
 'cash_from_operations':'Operating cash flow / 经营现金流',
 'capex':'Capital expenditures (positive outflow) / 资本开支',
 'cash':'Cash / 现金', 'total_assets':'Total assets / 总资产',
 'total_liabilities':'Total liabilities / 总负债', 'total_equity':'Total equity / 股东权益'
}
_D61_REQUIRED = ['fiscal_year','revenue','cash_from_operations','capex']
_D61_ALL = ['fiscal_year'] + list(_D61_FIELDS)
_D61_TEMPLATE = pd.DataFrame([
 {'fiscal_year':2023,'revenue':1000,'cogs':620,'operating_income':170,'net_income':125,'cash_from_operations':180,'capex':65,'cash':220,'total_assets':1400,'total_liabilities':650,'total_equity':750},
 {'fiscal_year':2024,'revenue':1100,'cogs':690,'operating_income':185,'net_income':139,'cash_from_operations':205,'capex':72,'cash':250,'total_assets':1550,'total_liabilities':720,'total_equity':830},
 {'fiscal_year':2025,'revenue':1200,'cogs':755,'operating_income':210,'net_income':155,'cash_from_operations':225,'capex':80,'cash':275,'total_assets':1690,'total_liabilities':780,'total_equity':910},
])
with st.expander('📘 输入格式、字段字典与演示模板',expanded=False):
 st.write('每行一个完整财年；金额全部使用同一报告货币及同一单位（例如 CNY millions）。CAPEX 填正数，表示现金流出。未提供的可选字段留空，不填 0。')
 st.dataframe(pd.DataFrame([{'field':k,'meaning':v,'required':k in _D61_REQUIRED} for k,v in [('fiscal_year','Fiscal year / 财年'),*_D61_FIELDS.items()]]),use_container_width=True,hide_index=True)
 st.download_button('⬇️ 下载演示 CSV（虚构数据）',_D61_TEMPLATE.to_csv(index=False).encode('utf-8-sig'),'AlphaLens_Day6_1_Template_FICTIONAL.csv','text/csv',key='d61_template')

_d61_c1,_d61_c2,_d61_c3=st.columns(3)
_d61_name=_d61_c1.text_input('Company / 公司名称',value='',key='d61_name')
_d61_ticker=_d61_c2.text_input('Ticker / 股票代码',value='',key='d61_ticker')
_d61_sector=_d61_c3.text_input('Sector / 行业',value='',key='d61_sector')
_d61_c4,_d61_c5,_d61_c6=st.columns(3)
_d61_ccy=_d61_c4.selectbox('Reporting currency / 报告币种',['CNY','USD','HKD','EUR','GBP','JPY','SGD','Other'],key='d61_ccy')
_d61_unit=_d61_c5.selectbox('Amount unit / 金额单位',['ones','thousands','millions','billions'],index=2,key='d61_unit')
_d61_source=_d61_c6.text_input('Source / 数据来源（URL 或报告名称）',key='d61_source')
_d61_upload=st.file_uploader('上传历史财务数据 CSV / XLSX',type=['csv','xlsx'],key='d61_upload')
_d61_demo=st.checkbox('使用虚构演示数据（不代表真实公司）',value=False,key='d61_demo')

_d61_raw=None
_d61_file_hash=None
_d61_issues=[]
if _d61_upload is not None:
 try:
  _d61_blob=_d61_upload.getvalue()
  _d61_file_hash=_hash61.sha256(_d61_blob).hexdigest()
  if _d61_upload.name.lower().endswith('.xlsx'):
   _d61_raw=pd.read_excel(_io61.BytesIO(_d61_blob),sheet_name=0)
  else:
   try:_d61_raw=pd.read_csv(_io61.BytesIO(_d61_blob),encoding='utf-8-sig')
   except UnicodeDecodeError:_d61_raw=pd.read_csv(_io61.BytesIO(_d61_blob),encoding='gb18030')
 except Exception as _d61_exc:
  st.error(f'无法读取文件: {_d61_exc}')
elif _d61_demo:
 _d61_raw=_D61_TEMPLATE.copy()
 _d61_file_hash=_hash61.sha256(_d61_raw.to_csv(index=False).encode()).hexdigest()

if _d61_raw is not None:
 _d61_raw.columns=[str(c).strip().lower() for c in _d61_raw.columns]
 _d61_missing=[c for c in _D61_REQUIRED if c not in _d61_raw.columns]
 _d61_unknown=[c for c in _d61_raw.columns if c not in _D61_ALL]
 if _d61_missing:_d61_issues.append(('ERROR','Missing required columns: '+', '.join(_d61_missing)))
 if _d61_unknown:_d61_issues.append(('INFO','Unmapped columns ignored: '+', '.join(_d61_unknown)))
 if not _d61_missing:
  _d61_df=_d61_raw.reindex(columns=_D61_ALL).copy()
  for _d61_col in _D61_ALL:_d61_df[_d61_col]=pd.to_numeric(_d61_df[_d61_col],errors='coerce')
  if _d61_df.empty:_d61_issues.append(('ERROR','No rows supplied'))
  if _d61_df['fiscal_year'].isna().any():_d61_issues.append(('ERROR','Invalid or missing fiscal_year'))
  if _d61_df['fiscal_year'].duplicated().any():_d61_issues.append(('ERROR','Duplicate fiscal_year'))
  if (_d61_df['fiscal_year'].dropna()%1!=0).any():_d61_issues.append(('ERROR','Fiscal year must be an integer'))
  for _d61_col in _D61_REQUIRED[1:]:
   if _d61_df[_d61_col].isna().any():_d61_issues.append(('ERROR',f'Missing/non-numeric required values in {_d61_col}'))
  if (_d61_df['revenue'].dropna()<=0).any():_d61_issues.append(('ERROR','Revenue must be positive'))
  if (_d61_df['capex'].dropna()<0).any():_d61_issues.append(('ERROR','CAPEX must be positive outflow; negative values found'))
  if (_d61_df['cogs'].dropna()<0).any():_d61_issues.append(('WARNING','Negative COGS found; check sign convention'))
  if _d61_df[['total_assets','total_liabilities','total_equity']].notna().all(axis=1).any():
   _d61_mask=_d61_df[['total_assets','total_liabilities','total_equity']].notna().all(axis=1)
   _d61_gap=(_d61_df['total_assets']-_d61_df['total_liabilities']-_d61_df['total_equity']).abs()
   _d61_tolerance=_d61_df['total_assets'].abs().clip(lower=1)*0.001
   if (_d61_gap[_d61_mask]>_d61_tolerance[_d61_mask]).any():_d61_issues.append(('WARNING','Balance sheet identity mismatch > 0.1% of assets'))
  _d61_df=_d61_df.sort_values('fiscal_year').reset_index(drop=True)
  _d61_df['fcf_proxy_cfo_less_capex']=_d61_df['cash_from_operations']-_d61_df['capex']
  _d61_df['revenue_growth_yoy']=_d61_df['revenue'].pct_change(fill_method=None)
  _d61_df['operating_margin']=_d61_df['operating_income']/_d61_df['revenue']
  _d61_df['fcf_proxy_margin']=_d61_df['fcf_proxy_cfo_less_capex']/_d61_df['revenue']
  _d61_errors=sum(level=='ERROR' for level,msg in _d61_issues)
  _d61_warnings=sum(level=='WARNING' for level,msg in _d61_issues)
  _d61_a,_d61_b,_d61_c=st.columns(3)
  _d61_a.metric('Fiscal years / 财年数',len(_d61_df))
  _d61_b.metric('Blocking errors / 阻断错误',_d61_errors)
  _d61_c.metric('Warnings / 警告',_d61_warnings)
  st.markdown('### Normalized financial statements / 标准化历史财务数据')
  st.dataframe(_d61_df,use_container_width=True,hide_index=True)
  st.markdown('### Data quality / 数据质量')
  if _d61_issues:st.dataframe(pd.DataFrame(_d61_issues,columns=['Severity','Issue']),hide_index=True,use_container_width=True)
  else:st.success('基础格式与会计恒等式检查通过。此结果不等于已核实财报真实性。')
  if not _d61_errors:
   _d61_chart=_d61_df.set_index('fiscal_year')[['revenue','fcf_proxy_cfo_less_capex']]
   st.markdown('### Historical trend / 历史趋势')
   st.line_chart(_d61_chart)
   _d61_meta={'module':'Day 6.1','company':_d61_name,'ticker':_d61_ticker,'sector':_d61_sector,'currency':_d61_ccy,'amount_unit':_d61_unit,'source':_d61_source,'file_sha256':_d61_file_hash,'imported_utc':_dt61.now(_tz61.utc).isoformat(),'fictional_demo':bool(_d61_upload is None and _d61_demo),'quality_issues':[{'severity':l,'message':m} for l,m in _d61_issues],'fcf_definition':'cash_from_operations - capex; not unlevered FCFF'}
   _d61_out=_d61_df.to_csv(index=False).encode('utf-8-sig')
   _d61_meta_bytes=_json61.dumps(_d61_meta,ensure_ascii=False,indent=2).encode('utf-8')
   _d61_x,_d61_y=st.columns(2)
   _d61_x.download_button('⬇️ 下载标准化财务数据 CSV',_d61_out,'AlphaLens_Day6_1_Normalized.csv','text/csv',key='d61_csv')
   _d61_y.download_button('⬇️ 下载数据审计 JSON',_d61_meta_bytes,'AlphaLens_Day6_1_Import_Audit.json','application/json',key='d61_json')
   st.info('本模块不自动将历史数据写入 Day 5 估值引擎；Day 6.4–6.6 完成预测、FCFF 与 DCF 接口后再联动。当前 FCF 仅为 CFO−CAPEX 的现金流代理指标。')
  else:st.error('存在阻断错误，请修复源文件后重新上传；禁止将该数据用于后续估值。')
else:st.info('上传 CSV / XLSX，或勾选虚构演示数据以检查 Day 6.1 工作流。')
st.caption('© 2026 Frida AlphaLens AI · Day 6.1 · User-supplied data; provenance not independently verified')


# === Day 6.2: Data Quality & Normalization (additive; Day 6.1 unchanged) ===
import json as _j62
import hashlib as _h62
from datetime import datetime as _dt62, timezone as _tz62

st.divider()
st.markdown('# Day 6.2 · Financial Data Quality & Normalization | 财务数据质量与标准化')
st.caption('独立检查上传文件或演示数据。此模块不修改 Day 5 DCF，也不自动将未经核验的数据写入估值引擎。')
_D62_ALIASES={
 'fiscal_year':['fiscal_year','year','fy','financial_year','财年','年度'],
 'revenue':['revenue','sales','net_sales','total_revenue','营业收入','收入'],
 'cogs':['cogs','cost_of_revenue','cost_of_sales','营业成本'],
 'operating_income':['operating_income','operating_profit','ebit','营业利润'],
 'net_income':['net_income','net_profit','净利润'],
 'cash_from_operations':['cash_from_operations','operating_cash_flow','cfo','cash_flow_from_operations','经营活动现金流量净额'],
 'capex':['capex','capital_expenditure','capital_expenditures','purchase_of_ppe','资本开支'],
 'cash':['cash','cash_and_equivalents','货币资金'],
 'total_assets':['total_assets','assets','资产总计'],
 'total_liabilities':['total_liabilities','liabilities','负债合计'],
 'total_equity':['total_equity','shareholders_equity','stockholders_equity','所有者权益'],
}
_D62_COLS=list(_D62_ALIASES)
_D62_REQ=['fiscal_year','revenue','cash_from_operations','capex']
_d62_input=_d61_raw.copy() if _d61_raw is not None else None
if _d62_input is None:
 st.info('先在 Day 6.1 上传 CSV/XLSX，或勾选虚构演示数据，然后查看 Day 6.2 质量诊断。')
else:
 _d62_input.columns=[str(x).strip() for x in _d62_input.columns]
 _d62_source_cols=list(_d62_input.columns)
 _d62_options=['— 不映射 —']+_d62_source_cols
 _d62_mapping={}
 _d62_auto_conflicts=[]
 with st.expander('1. 字段映射 / Column mapping',expanded=True):
  st.caption('自动识别常见中英文字段；请人工确认。每个原始字段只能映射到一个标准字段。')
  _d62_mcols=st.columns(3)
  for _d62_i,_d62_field in enumerate(_D62_COLS):
   _d62_matches=[c for c in _d62_source_cols if c.strip().lower().replace(' ','_') in [a.lower() for a in _D62_ALIASES[_d62_field]]]
   _d62_default=_d62_matches[0] if len(_d62_matches)==1 else '— 不映射 —'
   if len(_d62_matches)>1:_d62_auto_conflicts.append(_d62_field)
   with _d62_mcols[_d62_i%3]:
    _d62_choice=st.selectbox(_d62_field,_d62_options,index=_d62_options.index(_d62_default),key='d62_map_'+_d62_field)
   if _d62_choice!='— 不映射 —':_d62_mapping[_d62_field]=_d62_choice
 _d62_issues=[]
 def _d62_issue(level,code,message):_d62_issues.append({'severity':level,'code':code,'detail':message})
 if len(set(_d62_mapping.values()))!=len(_d62_mapping):_d62_issue('BLOCK','DUPLICATE_MAPPING','同一原始字段被映射到多个标准字段')
 for _d62_f in _D62_REQ:
  if _d62_f not in _d62_mapping:_d62_issue('BLOCK','MISSING_FIELD',f'缺少必填字段: {_d62_f}')
 if _d62_auto_conflicts:_d62_issue('WARN','AMBIGUOUS_ALIAS','多个候选字段需确认: '+', '.join(_d62_auto_conflicts))
 _d62_meta_cols=st.columns(3)
 _d62_period=_d62_meta_cols[0].selectbox('数据期间 / Period',['Annual','Quarterly','TTM'],key='d62_period')
 _d62_capex_sign=_d62_meta_cols[1].selectbox('CAPEX 符号约定',['正数表示流出','负数表示流出（转换为正）'],key='d62_capex_sign')
 _d62_strict=_d62_meta_cols[2].checkbox('严格模式：警告也阻断导出',value=False,key='d62_strict')
 if _d62_period!='Annual':_d62_issue('BLOCK','PERIOD_UNSUPPORTED','本版只接受完整年度财务数据；季度与 TTM 不能直接混入年度模型')
 _d62_df=pd.DataFrame(index=_d62_input.index)
 for _d62_f in _D62_COLS:
  if _d62_f in _d62_mapping:
   _d62_src=_d62_input[_d62_mapping[_d62_f]]
   _d62_numeric=pd.to_numeric(_d62_src.astype(str).str.replace(',','',regex=False).str.strip(),errors='coerce')
   _d62_invalid=_d62_src.notna() & _d62_src.astype(str).str.strip().ne('') & _d62_numeric.isna()
   if _d62_invalid.any():_d62_issue('BLOCK' if _d62_f in _D62_REQ else 'WARN','NON_NUMERIC',f'{_d62_f}: {_d62_invalid.sum()} 个非数值单元格')
   _d62_df[_d62_f]=_d62_numeric
  else:_d62_df[_d62_f]=float('nan')
 if _d62_capex_sign.startswith('负数'):
  _d62_df['capex']=-_d62_df['capex']
  _d62_issue('INFO','CAPEX_SIGN','按用户指定符号约定转换 CAPEX')
 if _d62_df.empty:_d62_issue('BLOCK','EMPTY','文件没有数据行')
 if _d62_df['fiscal_year'].isna().any():_d62_issue('BLOCK','INVALID_YEAR','财年存在缺失或非数值')
 if _d62_df['fiscal_year'].dropna().duplicated().any():_d62_issue('BLOCK','DUPLICATE_YEAR','财年重复')
 if (_d62_df['fiscal_year'].dropna()%1!=0).any():_d62_issue('BLOCK','YEAR_INTEGER','财年必须为整数')
 for _d62_f in _D62_REQ[1:]:
  if _d62_df[_d62_f].isna().any():_d62_issue('BLOCK','MISSING_REQUIRED',f'{_d62_f} 缺失或无效')
 if (_d62_df['revenue'].dropna()<=0).any():_d62_issue('BLOCK','REVENUE_SIGN','收入必须大于零')
 if (_d62_df['capex'].dropna()<0).any():_d62_issue('BLOCK','CAPEX_SIGN_INVALID','转换后 CAPEX 仍为负数；检查符号约定')
 if (_d62_df['cogs'].dropna()<0).any():_d62_issue('WARN','NEGATIVE_COGS','营业成本存在负数')
 _d62_bs=_d62_df[['total_assets','total_liabilities','total_equity']]
 _d62_mask=_d62_bs.notna().all(axis=1)
 if _d62_mask.any():
  _d62_gap=(_d62_df['total_assets']-_d62_df['total_liabilities']-_d62_df['total_equity']).abs()
  _d62_tol=_d62_df['total_assets'].abs().clip(lower=1)*0.001
  if (_d62_gap[_d62_mask]>_d62_tol[_d62_mask]).any():_d62_issue('WARN','BALANCE_SHEET','资产不等于负债加权益（超过资产的0.1%）')
 else:_d62_issue('INFO','BS_NOT_TESTED','缺少完整资产负债表字段，未进行恒等式检查')
 if (_d62_df['operating_income'].notna() & (_d62_df['operating_income'].abs()>_d62_df['revenue'].abs()*2)).any():_d62_issue('WARN','OPERATING_MARGIN','营业利润绝对值超过收入两倍，建议核实')
 _d62_df=_d62_df.sort_values('fiscal_year').reset_index(drop=True)
 _d62_years=_d62_df['fiscal_year'].dropna()
 if len(_d62_years)>1 and (_d62_years.diff().dropna()>1).any():_d62_issue('WARN','YEAR_GAPS','历史财年不连续')
 _d62_df['fcf_proxy_cfo_less_capex']=_d62_df['cash_from_operations']-_d62_df['capex']
 _d62_df['revenue_growth_yoy']=_d62_df['revenue'].pct_change(fill_method=None)
 if (_d62_df['revenue_growth_yoy'].abs()>1).any():_d62_issue('WARN','REVENUE_JUMP','收入同比变动超过100%，建议核实口径或异常值')
 _d62_blocks=sum(x['severity']=='BLOCK' for x in _d62_issues)
 _d62_warns=sum(x['severity']=='WARN' for x in _d62_issues)
 _d62_checks=9
 _d62_score=max(0,round(100-20*_d62_blocks-5*_d62_warns))
 _d62_ready=_d62_blocks==0 and (not _d62_strict or _d62_warns==0)
 _d62_metrics=st.columns(4)
 _d62_metrics[0].metric('质量评分 / 100',_d62_score)
 _d62_metrics[1].metric('阻断错误',_d62_blocks)
 _d62_metrics[2].metric('警告',_d62_warns)
 _d62_metrics[3].metric('导出状态','READY' if _d62_ready else 'BLOCKED')
 st.caption('评分是透明的启发式检查分（100 − 20×阻断项 − 5×警告项），不是财报真实性或市场可靠性评分。')
 st.markdown('### 2. 质量检查报告')
 if _d62_issues:st.dataframe(pd.DataFrame(_d62_issues),use_container_width=True,hide_index=True)
 else:st.success('已执行的规则未发现异常；仍需独立核验来源和会计口径。')
 st.markdown('### 3. 标准化结果预览')
 st.dataframe(_d62_df,use_container_width=True,hide_index=True)
 _d62_audit={'module':'Day 6.2','timestamp_utc':_dt62.now(_tz62.utc).isoformat(),'fictional_demo':bool(_d61_upload is None and _d61_demo),'source':_d61_source,'company':_d61_name,'ticker':_d61_ticker,'currency':_d61_ccy,'amount_unit':_d61_unit,'period':_d62_period,'capex_sign':_d62_capex_sign,'source_sha256':_d61_file_hash,'mapping':_d62_mapping,'unmapped_columns':[c for c in _d62_source_cols if c not in _d62_mapping.values()],'issues':_d62_issues,'score':_d62_score,'ready_for_export':_d62_ready,'fcf_definition':'CFO minus CAPEX proxy, NOT unlevered FCFF','checks_scope':'internal format and arithmetic only; source authenticity not verified'}
 if _d62_ready:st.success('内部格式与规则检查达到导出门槛；并不代表真实财报已核验，也不自动连接 DCF。')
 else:st.error('存在阻断项；请修复数据或映射后再导出标准化结果。')
 _d62_dl1,_d62_dl2=st.columns(2)
 _d62_dl1.download_button('⬇️ Day 6.2 标准化 CSV',_d62_df.to_csv(index=False).encode('utf-8-sig'),'AlphaLens_Day6_2_Normalized.csv','text/csv',disabled=not _d62_ready,key='d62_csv')
 _d62_dl2.download_button('⬇️ Day 6.2 审计 JSON',_j62.dumps(_d62_audit,ensure_ascii=False,indent=2).encode('utf-8'),'AlphaLens_Day6_2_Audit.json','application/json',key='d62_audit')
 st.caption('Day 6.2 prototype · No external verification · No automatic DCF linkage')

# === Day 6.3: Historical Financial Diagnostics (submission-ready) ===
st.divider()
st.markdown('## Day 6.3 · Historical Financial Diagnostics | 历史财务诊断')
st.caption('基于 Day 6.2 标准化结果的描述性分析；不自动修改 Day 5 DCF。')
if _d62_input is None:
    st.info('请先在 Day 6.1 上传财务数据，或勾选虚构演示数据。')
elif not _d62_ready:
    st.warning('Day 6.2 尚有阻断错误；请先完成数据质量检查。')
else:
    _d63 = _d62_df.copy().sort_values('fiscal_year')
    _d63['gross_margin'] = (_d63['revenue'] - _d63['cogs']) / _d63['revenue']
    _d63['operating_margin'] = _d63['operating_income'] / _d63['revenue']
    _d63['net_margin'] = _d63['net_income'] / _d63['revenue']
    _d63['cfo_margin'] = _d63['cash_from_operations'] / _d63['revenue']
    _d63['fcf_proxy_margin'] = _d63['fcf_proxy_cfo_less_capex'] / _d63['revenue']
    _d63['capex_intensity'] = _d63['capex'] / _d63['revenue']
    _d63['cash_conversion_cfo_to_ni'] = _d63['cash_from_operations'] / _d63['net_income'].replace(0, float('nan'))
    _d63_last = _d63.iloc[-1]
    _d63_metrics = st.columns(4)
    _d63_metrics[0].metric('最新财年收入', f"{_d63_last['revenue']:,.1f} {_d61_unit}")
    _d63_metrics[1].metric('收入同比', f"{_d63_last['revenue_growth_yoy']:.1%}" if pd.notna(_d63_last['revenue_growth_yoy']) else 'N/A')
    _d63_metrics[2].metric('营业利润率', f"{_d63_last['operating_margin']:.1%}" if pd.notna(_d63_last['operating_margin']) else 'N/A')
    _d63_metrics[3].metric('CFO − CAPEX', f"{_d63_last['fcf_proxy_cfo_less_capex']:,.1f} {_d61_unit}")
    st.markdown('### Revenue & cash flow | 收入与现金流')
    _d63_plot = go.Figure()
    _d63_x = _d63['fiscal_year'].astype('Int64').astype(str)
    _d63_plot.add_trace(go.Bar(x=_d63_x, y=_d63['revenue'], name='Revenue', marker_color=BLUE))
    _d63_plot.add_trace(go.Scatter(x=_d63_x, y=_d63['cash_from_operations'], name='CFO', mode='lines+markers', line=dict(color=TEAL, width=3)))
    _d63_plot.add_trace(go.Scatter(x=_d63_x, y=_d63['fcf_proxy_cfo_less_capex'], name='CFO − CAPEX', mode='lines+markers', line=dict(color=RED, width=3)))
    st.plotly_chart(format_plot(_d63_plot, 'Historical performance', 390), use_container_width=True)
    st.markdown('### Profitability & cash conversion | 盈利与现金转化')
    _d63_view = ['fiscal_year', 'revenue_growth_yoy', 'gross_margin', 'operating_margin', 'net_margin', 'cfo_margin', 'fcf_proxy_margin', 'capex_intensity', 'cash_conversion_cfo_to_ni']
    st.dataframe(_d63[_d63_view].style.format({c:'{:.1%}' for c in _d63_view[1:-1]} | {'cash_conversion_cfo_to_ni':'{:.2f}x'}, na_rep='N/A'), use_container_width=True, hide_index=True)
    _d63_flags = []
    if len(_d63) < 3: _d63_flags.append('历史年度少于三年，趋势判断证据有限。')
    if (_d63['fcf_proxy_cfo_less_capex'] < 0).any(): _d63_flags.append('部分年份 CFO − CAPEX 为负，请检查投资周期及经营现金流。')
    if (_d63['cash_conversion_cfo_to_ni'] < 0.8).any(): _d63_flags.append('部分年份 CFO / 净利润低于 0.8，建议核查营运资本及非现金项目。')
    if _d63['gross_margin'].isna().all(): _d63_flags.append('缺少 COGS，无法计算毛利率。')
    st.markdown('### Research notes | 研究提示')
    if _d63_flags:
        for _d63_flag in _d63_flags: st.warning(_d63_flag)
    else: st.success('未触发本模块的简单趋势提示；这不代表财务质量或数据真实性已经核验。')
    st.info('CFO − CAPEX 是现金流代理指标，不等于无杠杆 FCFF。财务数据及来源仍需独立核验；本模块不构成投资建议。')
    _d63_export = {'module':'Day 6.3','company':_d61_name or ('Fictional Demo' if _d61_demo and _d61_upload is None else 'Unspecified'), 'currency':_d61_ccy, 'amount_unit':_d61_unit, 'source':_d61_source, 'fictional_demo':bool(_d61_demo and _d61_upload is None), 'data_quality_score':_d62_score, 'historical_years':len(_d63), 'research_flags':_d63_flags, 'note':'Internal diagnostics only; not verified market data or unlevered FCFF.'}
    _d63_a, _d63_b = st.columns(2)
    _d63_a.download_button('⬇️ 下载 Day 6.3 财务诊断 CSV', _d63.to_csv(index=False).encode('utf-8-sig'), file_name='AlphaLens_Day6_3_Diagnostics.csv', mime='text/csv', key='d63_csv')
    _d63_b.download_button('⬇️ 下载 Day 6.3 摘要 JSON', json.dumps(_d63_export, ensure_ascii=False, indent=2).encode('utf-8'), file_name='AlphaLens_Day6_3_Summary.json', mime='application/json', key='d63_json')
st.caption('© 2026 Frida AlphaLens AI · Day 6.3 · Educational research prototype')
