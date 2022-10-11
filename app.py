import pickle
import  streamlit as st
import  numpy as np


df=pickle.load(open('df.pkl', 'rb'))
model=pickle.load(open('model.pkl','rb'))



st.header('Laptop Price ')

company=st.selectbox('Select Company',options=df['Company'].unique()) 
type=st.selectbox('Select type',options=df['TypeName'].unique())
screen_size=st.selectbox('Select screen',options=df['Inches'].unique())
ram=st.selectbox('Select ram',options=df['Ram'].unique())
sys=st.selectbox('Select oprating system',options=df['OpSys'].unique())
weight=st.selectbox('Select weight Kg',options=round(df['Weight'],0))
touchscreen=st.selectbox('Touch screen',options=['Yes','No'])

ips=st.selectbox('IPS',options=['Yes','No'])
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu=st.selectbox('Cpu Gen',df['cpu_gen'].unique())
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu=st.selectbox('Select Company',options=df['GPU Brand'].unique()) 

if st.button('Predict Price'):
    # query
    # ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res =int(resolution.split('x')[0])
    Y_res =int(resolution.split('x')[1])
    
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,screen_size,ram,sys,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu])

    query = query.reshape(1,13)
    a=np.array(query,dtype='object')
    st.title(round(np.exp(model.predict(a)[0]),0))


# a=resolution.split('x')[1]
# print(a)