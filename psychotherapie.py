import streamlit as st
import pandas as pd

st.header("Jährlicher Anteil der Kinder und Jugendlichen mit Psychotherapie in Prozent")
st.subheader("immer mehr Psychotherapie für Jugendliche")

chart_data = pd.DataFrame({
    'date': ['2009-01-01', '2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01', '2018-01-01', '2019-01-01'],
    'Psychotherapie im erweiterten Sinne*': [2.03, 2.17, 2.31, 2.40, 2.48, 2.59, 2.71, 2.80, 3.35, 3.85, 4.13],
    'Psychotherapie im engeren Sinne**': [1.31, 1.38, 1.46, 1.52, 1.55, 1.61, 1.69, 1.76, 1.78, 1.82, 1.92]
})

chart_data['date'] = pd.to_datetime(chart_data['date'])
chart_data = chart_data.set_index('date')

st.line_chart(chart_data)

txt = st.text_area('', '''
    /
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: BARMER")