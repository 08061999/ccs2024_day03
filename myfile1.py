# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:25:41 2024

@author: user
"""

import matplotlib.pyplot as plt

react_conv= [0.5,0.6,0.7,0.7,0.9]
temp = [180,200, 220, 240,260]

#plt.plot(temp,react_conv)

#plt.xlabel("temperature")

#plt.ylabel("reaction conversion")

#plt.title("chemical experiment")

#plt.show()



import plotly.express as px 

#fig = px.line(x = temp, y = react_conv)

#fig.write_html("plot.html")


# day1_attendees = [70, 20, 64, 90, 80]
# day1_names = ["blessing", "mali", "pangi", "tafi", "shini"]

# plt.bar(day1_names, day1_attendees)

# plt.show()



x_scatter= [1,2,3,4,5]

y_scatter = [2,4,6,8,10]

plt.scatter(x_scatter, y_scatter)

plt.show

import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")

