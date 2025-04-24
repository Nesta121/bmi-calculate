import streamlit as st
bg="""
<style> 
.stApp {
    background-image: url("https://i.pinimg.com/736x/fd/af/73/fdaf731adbe8fff9840445de261e4610.jpg")
    background-size: cover;
    background-position: no-repeat;
    background-attachment: fixed;
st.title("BMI Calculation")
st.markdown("---")

kg=st.number_input("Weight(Kg.)",value=60.5,min_value=10.0,max_value=200.0,step=0.5)
cm=st.number_input("Height(Cm.)",value=100,min_value=1,max_value=200,step=1)

if st.button("Calculate"):
    b=kg/(cm/100)**2
    st.subheader(f"ค่าดัชนีของคุณคือ {b:.1f}")
    
    if b<18.5:
        st.info("น้อยไป")
        st.warning("เสี่ยงขาดสารอาหาร")
        st.image("1.png")
    elif b<23:
        st.info("ปกติ")
        st.success("มีโอกาสเกิดโรคแทรกซ้อนน้อยที่สุด")
        st.image("2.png")
    elif b<25:
        st.info("เริ่มอ้วน")
        st.warning("ภาวะน้ำหนักเกินมีโรคแทรกซ้อน")
        st.image("3.png")
    elif b<30:
        st.info("อ้วน")
        st.warning("มีโอกาสเกิดโรคสูง")
        st.image("4.png")
    else:
        st.info("อ้วนมาก")
        st.error("เสี่ยงต่อโรคร้าย")
        st.image("5.png")
    
    





    


                
