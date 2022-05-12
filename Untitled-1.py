# %%
import streamlit as st
from collections import Counter
from PIL import Image
import numpy as np
import pandas as pd
import json
import requests as r
import time
from datetime import datetime

# %%
# выбор даты начала

start_day = st.date_input(
     "Дата начала",)
st.write('Воронка с', start_day, 'числа')

# %%
# выбор даты конца

end_day = st.date_input(
     "Дата конца",)
st.write('Воронка до', end_day, 'числа')

# %%
# загрузка событий из AppMetrica

# but = st.button("Загрузить данные")

# if but:
#     while True:
#         header={
#             'Content-Type': 'application/x-yametrika+json',
#             'Authorization': 'OAuth AQAEA7qjKZXKAAfhX_j1dIIUR059lNONgVpbkWk'
#         }
#         metrika_url = f'https://api.appmetrica.yandex.ru/logs/v1/export/events.json?application_id=4065523&date_since={start_day}%2000%3A00%3A00&date_until={end_day}%2023%3A59%3A59&date_dimension=default&use_utf8_bom=true&fields=appmetrica_device_id%2Ccity%2Cevent_name'

#         #st.spinner('Wait for it...')

#         res = r.get(metrika_url, headers=header)
#         if res.status_code == 200:
#             items = json.loads(res.text.lstrip('\ufeff'))
#             df = pd.DataFrame.from_dict(items['data'])
#             st.write(df)
#             break
#         time.sleep(300)

# %%
df = pd.read_csv('events (3).csv')

# %%
df.info()

# %%
# selected_sn = col_multi.selectbox(
#     "Выберите конкурента",
#     options=pivot_sn_day.shop_network_name.unique().tolist(),
#     index=0,
# )

# %%
first_step = st.multiselect('Выберите событие для первого шага',df.event_name.unique().tolist())
second_step = st.multiselect('Выберите событие для второго шага',df.event_name.unique().tolist())
third_step = st.multiselect('Выберите событие для третьего шага',df.event_name.unique().tolist())
fourth_step = st.multiselect('Выберите событие для четвертого шага',df.event_name.unique().tolist())
fifth_step = st.multiselect('Выберите событие для пятого шага',df.event_name.unique().tolist())
sixth_step = st.multiselect('Выберите событие для шестого шага',df.event_name.unique().tolist())
seventh_step = st.multiselect('Выберите событие для седьмого шага',df.event_name.unique().tolist())



