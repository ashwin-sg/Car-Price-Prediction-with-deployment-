import streamlit as st
import joblib





def main():

    st.title("Used Car Price Prediction")



    html_temp = """
  
    }
    </style>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    Fuel_Type = st.selectbox("Select Type of Fuel", ['Select Fuel','Petrol', 'Diesel', 'CNG', 'LPG'])
  
    Transmission = st.selectbox("Transmission", ["Select Transmission",'Manual', 'Automatic'])
    
    Owner_Type = st.text_input("Enter Number of Previous Owner/Owners - for example: 1,2 or 3 etc.", "")

    Seats = st.text_input("Enter Number of Desired Seats from options (2,4,5,6,7,8,9,10)", "")

    Age = st.text_input("Age of Car in Years (select between 1 to 22)", "")

    Engine_CC = st.selectbox("Select the Engine Capacity in CC", ['select', 750, 1000, 1200, 1500, 1800, 2500, 3500, 4500, 5500])

    Kms_Driven = st.selectbox("Select Total Kilometers Driven by the Car", ['select', 10000, 20000, 30000, 40000, 50000, 75000, 100000, 150000])


    if st.button('Predict'):
        model = joblib.load('price_model.ml')
        output = round(model.predict([[Fuel_Type, Transmission, Owner_Type, Seats, Brand, Age, Engine_CC, Kms_Driven]])[0],2)
        st.success("The predicted price of the desired used car in lakhs INR is {}".format(output))

    if st.button('About'):
        st.success("Made by Ashwin Ghonmode - A Data Science Enthusiast")
        st.success("Github Link: https://github.com/ashwin-sg/Used-Car-Price-Prediction ")


if __name__=="__main__":
    main()
