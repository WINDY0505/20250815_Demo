import numpy as np
import pandas as pd
import streamlit as st

st.title("DEMO PAGE")
st.write("## This is a demo page for the Streamlit application.")  
st.write("You can use this page to test various features of Streamlit.")

arr1=np.array([1, 2, 3, 4, 5])
st.write("Here is a NumPy array:")
st.write(arr1)

df1=pd.DataFrame([[11,22,33,44,55], [50,60,70,80,90]], columns=['a', 'b', 'c', 'd', 'e'], index=['row1', 'row2']    )
st.write(df1)
st.table(df1)
      

st.write("## 核取方塊")
r1=st.checkbox("外帶")
if r1:
    st.info("外帶")
else:
    st.info("內用")


checks=st.columns(3)
txt=""
with checks[0]:
    r11=st.checkbox("A")
    if r11:
        txt+="A "
with checks[1]:
    r12=st.checkbox("B")
    if r12:
        txt+="B"
with checks[2]:      
    r13=st.checkbox("C")
    if r13:
        txt+=" C"
st.info(txt)

st.write("## 單選按鈕")
b1=st.radio("飲料", ["果汁", "可樂", "咖啡", "茶"])
st.info(b1)
b2=st.radio("飲料", ["果汁", "可樂", "咖啡", "茶"],key="drink2")
st.info(b2)

st.write("## 多選按鈕")
c1=st.multiselect("飲料", ["果汁", "可樂", "咖啡", "茶"])
st.info(c1)

st.sidebar.write("## 滑桿")
num=st.sidebar.slider("請選擇數量:", 0, 100, 50, step=5)
st.sidebar.info(num)


st.sidebar.write("## 下拉選單")
select1=st.sidebar.selectbox("請選擇飲料", ["果汁", "可樂", "咖啡", "茶","others"])
if select1 == "果汁":
    st.sidebar.info("你選擇了果汁")
elif select1 == "可樂":
    st.sidebar.info("你選擇了可樂")
elif select1 == "咖啡":
    st.sidebar.info("你選擇了咖啡")
elif select1 == "茶":
    st.sidebar.info("你選擇了茶")
else:
    st.sidebar.info("你選擇了其他")

st.write("## 按鈕")
a=st.number_input("unm.......",step=1, format="%d")
b=st.number_input("unm.......",step=1, format="%d",key="b")
if st.button("相加"):
    st.info(f"### 結果是: {a+b}")