import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import altair as alt

st.title("Customer Profile Analysis for Hotel Reservation Cancellations")
# # st.text("This is a web app to understand the typical profiles of customers who are more likely to cancel their bookings.")
st.markdown("This is a web app to understand the typical profiles of customers who are more likely to cancel their bookings.")

df = pd.read_csv("Hotel_Reservations_finalclean.txt")
df["long_trip"] = (df["weekend_nights_no"] + df["weekday_nights_no"]) > 2
df_interest = df.filter(["lead_time", "avg_price_per_room", "special_requests_no", "month", "prev_show_rate", "long_trip" ,"canceled"])

# Target Variable
df_interest_canceled = df[df["canceled"] == 0]
df_interest_commited = df[df["canceled"] == 1]

# # st.header("The Dataset:")
# st.markdown("## The Dataset:")
# st.write(df_interest)


# #***Visual 1 - "Distributions of Special Requests by Cancellations and Commmitments8***
# labels = ['Cancelled', 'Commit']
# fig, ax = plt.subplots(1,1)
# ax.boxplot([df_interest_canceled["special_requests_no"], df_interest_commited["special_requests_no"]], labels=labels)
# # plt.ylim(0, 2)  # set the y-axis limits
# # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
# ax.set_xlabel("Booking Status")
# ax.set_title("Distributions of Special Requests by Cancellations and Commmitments")
# #st.markdown("**Distributions of Special Requests by Cancellations and Commmitments**")
# #plt.show()
# st.pyplot(fig)
#
#
# #*******Visual 2 - Distributions of Lead Time by Cancellations and Commmitments*********
# fig, ax = plt.subplots(1,1)
# ax.boxplot([df_interest_canceled["lead_time"], df_interest_commited["lead_time"]], labels=labels)
# # plt.ylim(0, 2)  # set the y-axis limits
# # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
# ax.set_xlabel("Booking Status")
# ax.set_title("Distributions of Lead Time by Cancellations and Commmitments")
# st.pyplot(fig)
#
#
# #*****Visual 3 - Distributions of Room price by Cancellations and Commmitments******
# fig, ax = plt.subplots(1,1)
# ax.boxplot([df_interest_canceled["avg_price_per_room"], df_interest_commited["avg_price_per_room"]], labels=labels)
# # plt.ylim(0, 2)  # set the y-axis limits
# # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
# ax.set_xlabel("Booking Status")
# ax.set_title("Distributions of Room price by Cancellations and Commmitments")
# plt.grid(axis='y')
# st.pyplot(fig)
st.write('I need to justify this somehow.')





col1, col2, col3 = st.columns(3)

with col1:
    labels = ['Cancelled', 'Commit']
    fig, ax = plt.subplots(1, 1)
    ax.boxplot([df_interest_canceled["special_requests_no"], df_interest_commited["special_requests_no"]],
               labels=labels)
    # plt.ylim(0, 2)  # set the y-axis limits
    # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
    ax.set_xlabel("Booking Status")
    ax.set_title("Distributions of Special Requests by Cancellations and Commmitments")
    # st.markdown("**Distributions of Special Requests by Cancellations and Commmitments**")
    # plt.show()
    plt.grid(axis='y')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(1, 1)
    ax.boxplot([df_interest_canceled["lead_time"], df_interest_commited["lead_time"]], labels=labels)
    # plt.ylim(0, 2)  # set the y-axis limits
    # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
    ax.set_xlabel("Booking Status")
    ax.set_title("Distributions of Lead Time by Cancellations and Commmitments")
    plt.grid(axis='y')
    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots(1, 1)
    ax.boxplot([df_interest_canceled["avg_price_per_room"], df_interest_commited["avg_price_per_room"]], labels=labels)
    # plt.ylim(0, 2)  # set the y-axis limits
    # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
    ax.set_xlabel("Booking Status")
    ax.set_title("Distributions of Room price by Cancellations and Commmitments")
    plt.grid(axis='y')

    st.pyplot(fig)
    #st.write('I need to justify this somehow.')


fig, ax = plt.subplots(1,1)
bar_df = pd.crosstab(index = df_interest["canceled"], columns= df_interest["long_trip"])
# w =bar_df.plot.bar( figsize = (7,4), rot = 0)
# ax.bar(figure,figsize = (7,4))
# st.pyplot(bar_df)
st.bar_chart(bar_df)




fig, ax = plt.subplots(1, 1)
figure2 = pd.crosstab(index = df_interest["canceled"], columns  = df_interest["month"])
canceled_total = 0
commited_total = 0
for i in range(1,13):
    canceled_total += figure2[i][1]
    commited_total += figure2[i][0]
print(figure2)
print(canceled_total)
print(commited_total)
for i in range(1,13):
    figure2[i][1] = 100 * figure2[i][1]/canceled_total
    figure2[i][0] = 100 * figure2[i][0]/commited_total
ax = figure2.plot.bar(figsize = (12,9), rot = 1, legend=("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"))
st.bar_chart(figure2)






sb.violinplot(data = df_interest, x = "canceled", y = "prev_show_rate")

