import pickle 
import streamlit as st 

model = pickle.load(open("spam.pkl","rb"))



def main():
    
    st.title("Spam Detection app")
    st.subheader("Built with streamlit and python")
    
    msg = st.text_input("Enter your text : ")
    
    if st.button("Predict"):
        prediction = model.predict([msg])
        
        if prediction==1:
            st.error("This is spam email")
        else:
            st.success("This is a genuine email")
    
main()