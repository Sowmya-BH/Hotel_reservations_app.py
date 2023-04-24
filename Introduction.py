import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import csv


st.title("Customer Profile Analysis for Hotel Reservation Cancellations")
st.markdown("This is a web app to understand the typical profiles of customers who are more likely to cancel their bookings.To acheive this we plan to classify the customers based on several characteristics, including room price, room type, previous cancelation, nights of stay, etc. The motivation behind the project, is to provide hotels with suggestions that can enhance their booking mechanisms")

df = pd.read_csv("Hotel_Reservations_finalclean.txt")


df["long_trip"] = (df["weekend_nights_no"] + df["weekday_nights_no"]) > 2
df_interest = df.filter(["lead_time", "avg_price_per_room", "special_requests_no", "month", "prev_show_rate", "long_trip" ,"canceled"])

# Target Variable
df_interest_canceled = df[df["canceled"] == 0]
df_interest_commited = df[df["canceled"] == 1]

# st.header("The Dataset:")
st.markdown("### The Dataset:")
st.write(df_interest)