import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# trigonometric array
x = np.linspace(0,360,100)
xrad = np.deg2rad(x)
y1 = np.sin(xrad)
y2 = np.cos(xrad)
# plot the function
plt.plot(xrad, y1)
plt.plot(xrad, y2)
plt.title("Trigonometric Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.style.use('seaborn')
plt.show()

# dataframe
name = ["Thehila","Ben", "Uwit", "Oatre"]
cars = [2,2,8,0]
age = [45,80,64,30]
trig = pd.DataFrame[{"Name":name, "Cars":cars, "Age":age}]
trig