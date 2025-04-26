import streamlit as st

st.title("Unit Convertor App")
st.markdown("### Converts length, weight And Time Instantantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

category = st.selectbox("Choose a categoty", ["length", "weight", "Time"])

def Convert_units(category, value, unit):
    if category == "length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
                 return value / 0.621371

        elif category == "Weight":
            if unit == "Kilograms to Pounds":
                    return value * 2.20462
            elif unit == "Pounds to Kilograms":
                    return value / 2.20462  
        elif category == "Time":
                if unit == "Seconds to mintues":
                 return value / 60
                elif unit == "Mintues to Seconds":
                 return value * 60
                elif unit == "Hours to Mintues":
                 return value / 60
                elif unit == "Mintues to Hours":
                 return value * 60
                elif unit == "Hours to Days":
                 return value / 24
                elif unit == "Days to Hours":
                 return value * 24

if category == "length":
    unit = st.selectbox("Select Conversation", ["kilometer to miles", "Miles to kilometers"])
elif  category  == "Weight":
    unit = st.selectbox("Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])   

elif category == "Time":
    unit = st.selectbox("Select Conversation", ["Seconds to Mintues", "Mintues to Seconds", "Hours to Mintues", "Mintues to Hours", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = Convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
