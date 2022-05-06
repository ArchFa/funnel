# %%
import pandas as pd
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
d = st.date_input(
     "When's your birthday",)
st.write('Your birthday is:', d)

# %%
# while True:
#     header={
#         'Content-Type': 'application/x-yametrika+json',
#         'Authorization': 'OAuth AQAEA7qjKZXKAAfhX_j1dIIUR059lNONgVpbkWk'
#     }

#     metrika_url = 'https://api.appmetrica.yandex.ru/logs/v1/export/events.json?application_id=4065523&date_since=2022-04-30%2000%3A00%3A00&date_until=2022-05-06%2023%3A59%3A59&date_dimension=default&use_utf8_bom=true&fields=appmetrica_device_id%2Ccity%2Cevent_name'

#     res = r.get(metrika_url, headers=header)
#     res
#     if res.status_code == 200:
#         break
#     time.sleep(300)


