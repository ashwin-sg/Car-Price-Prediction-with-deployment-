import streamlit as st
import joblib





def main():

    st.title("Used Car Price Prediction")



    html_temp = """
       <style>
    body {
    background-image: url("https://wallpapercave.com/wp/H6Rj7PM.jpg");
    background-size: auto;
  
    }
    </style>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    Fuel_Type = st.selectbox("Select Type of Fuel", ['Select Fuel','Petrol', 'Diesel', 'CNG', 'LPG'])
    if (Fuel_Type == 'Petrol'):
        Fuel_Type=3
    elif (Fuel_Type == 'Diesel'):
        Fuel_Type=1
    elif (Fuel_Type == 'LPG'):
        Fuel_Type=2
    else:
        Fuel_Type=0

    Transmission = st.selectbox("Transmission", ["Select Transmission",'Manual', 'Automatic'])
    if (Transmission=='Manual'):
        Transmission=1
    else:
        Transmission=0

    Owner_Type = st.text_input("Enter number of previous owner/owners - for example: 1,2 or 3 etc.", "")

    Seats = st.text_input("Enter number of desired seats from options (2,4,5,6,7,8,9,10)", "")

    Brand = st.selectbox("Select Car Brand/ Compnay", ['select','Maruti','Hyundai', 'Honda', 'Toyota', 'Mercedes-Benz','Volkswagen'])
    if (Brand=='Maruti'):
        Brand = 2
    elif (Brand=='Hyundai'):
        Brand = 1
    elif (Brand == 'Honda'):
        Brand = 0
    elif (Brand == 'Toyota'):
        Brand = 3
    elif (Brand == 'Volkswagen'):
        Brand = 4
    else:
        Brand = 5

    Age = st.text_input("Age of Car in Years (select between 1 to 22)", "")

    Engine_CC = st.selectbox("Select the engine capacity in CC", ['select', 750, 1000, 1200, 1500, 1800, 2500, 3500, 4500, 5500])

    Kms_Driven = st.selectbox("Select cars' total kilometers driven", ['select', 10000, 20000, 30000, 40000, 50000, 75000, 100000, 150000])


    if st.button('Predict'):
        model = joblib.load('price_model.ml')
        output = round(model.predict([[Fuel_Type, Transmission, Owner_Type, Seats, Brand, Age, Engine_CC, Kms_Driven]])[0],2)
        st.success("The predicted price of the desired used car in lakhs INR is {}".format(output))

    if st.button('About'):
        st.success("Made by Ashwin Ghonmode - A Data Science Enthusiast")
        st.success("Github Link: ")


if __name__=="__main__":
    main()