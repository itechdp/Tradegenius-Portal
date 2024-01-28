import streamlit as st

def get_decimal_places(value):
    if '.' in str(value):
        return len(str(value).split('.')[1])
    else:
        return 0
st.set_page_config(
    page_title="Trade Genius  Portal",
    page_icon="📊",
    )

st.write("<h1 style='text-align:Center'>Trade Genius Portal 📊</h1>",unsafe_allow_html=True)
value = st.number_input("Enter Your Value:")
coin_name = st.text_input("Enter Coin Name:")
types = st.selectbox(label='Select LONG or SHORT',options=['LONG',"SHORT"])
if types == "LONG":
    st.write(f'''<b>
KiteKraken 👑 Premium   
<br> COIN: ${coin_name}/USDT   
<br> {types}: Up to 10X (Isolated)   
<br> Exchange: BINANCE    
<br> ➖➖➖➖➖➖➖➖➖➖➖   
<br> <b>ENTRY -    {value}\n</b>
<br> <b>TARGET 1 - {round(1.01*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 2 - {round(1.02*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 3 - {round(1.05*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 4 - {round(1.10*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 5 - {round(1.20*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>SL - {round(0.90*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> ➖➖➖➖➖➖➖➖➖➖➖
<br> 
<br> 👉DM with any questions :</b> @KiteKraken
    ''',unsafe_allow_html=True)

elif types == 'SHORT':
        st.write(f'''<b>
KiteKraken 👑 Premium   
<br> COIN: ${coin_name}/USDT   
<br> {types}: Up to 10X (Isolated)   
<br> Exchange: BINANCE    
<br> ➖➖➖➖➖➖➖➖➖➖➖   
<br> <b>ENTRY -    {value}\n</b>
<br> <b>TARGET 1 - {round(0.99*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 2 - {round(0.98*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 3 - {round(0.95*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 4 - {round(0.90*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>TARGET 5 - {round(0.80*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> <b>SL - {round(1.10*value,ndigits=get_decimal_places(value=value))}\n</b>
<br> ➖➖➖➖➖➖➖➖➖➖➖
<br> 
<br> 👉DM with any questions :</b> @KiteKraken
    ''',unsafe_allow_html=True)
st.write("© 2024 TradeGenius Portal - By Dhrumil Patel")

