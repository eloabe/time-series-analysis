import os
import pickle
import datetime

import pandas as pd
import streamlit as st

MODEL_DIR = r'C:\Users\Eloabe\Desktop\repos\projetos\time-series-analysis\data_app\model\model.pkl'

model = pickle.load(open(MODEL_DIR, 'rb'))

st.title("Predição de refeições do RU da UFC")
st.subheader("Aplicativo que prevê a quantidade de refeições feitas em um dia no RU")

date = st.date_input(
    "Insira a data",
    datetime.date(2023, 7, 6)
)

df = pd.DataFrame(
    {
        'year': date.year,
        'month': date.month,
        'day': date.day,
        'weekday': date.weekday()
    },
    index = [date]
)

result = int( model.predict(df) )

st.write(f'No dia {date}, serão feitas {result} refeições.')