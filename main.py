import streamlit as st
import pandas as pd

with st.echo():
    #ใช้ css ร่วม
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # ตั้งชื่อ TOPIC Website
    st.title("Learn Streamlit Basic")

    #label
    st.write("คำสั่งเบื้องต้น")

    #markdown
    st.markdown("Python : Function")

    #Button
    run_streamlit =st.button("Show me")

    if run_streamlit :
        #code
        show_code = '''def Hello(name):
        print("Hello"+name)
        
    Hello("Aum")'''
        st.code(show_code,language="python")

    st.markdown("<h3 style='text-align: center;'>NLP TASK</h3>",unsafe_allow_html=True)

    #ทำให้เป็นแนวนอน
    cols = st.columns(3) #เลขในวงเล็บคือจำนวนกี่ cloumn

    with cols[0]: #เรียกใช้โดยใช้index
        #input 
        # min_value = 0 => number_input = int 
        text = st.text_input("Input Name : ",placeholder="Input Your Name")
        
        
    with cols[1]:
        age = st.number_input("Input your age : ", min_value=0 , placeholder="")
        word_tokenize = "|".join(text.split()) # .split คือการตัดคำที่ก่อนเว้นวรรคเป็นหนึ่งคำ แล้วบันทึกลงใน list , "|".join คือการใส่ | แทนช่องว่าง

    st.markdown(f"Hello , {text} ! How are you today? You're {age} years old.")
    st.markdown(f"{word_tokenize}")

    #สร้างตาราง
    data = pd.DataFrame({
        "Nick Name" : ["Aum" , "Min", "Titan",f"{text}"],
        "Age" : [17,17,17,f"{age}"]
    })

    st.dataframe(data, use_container_width=True) #use_container_width = True ทำให้ตารางเต็ม cloumn แล้วอยู่ตรงกลาง

    show_chart = st.button(label="Show Chart")
    if show_chart:
        st.line_chart(data,x="Nick Name",y="Age")