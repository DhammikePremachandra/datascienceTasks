import matplotlib.pyplot as plt
import numpy as np

#P reparing the data.
x = np.linspace(0, 100, 100) #x axis
y = np.sin(x) # y values

# Plotting the data.
plt.plot(x, y, label="sine")
# Creating a title.
plt.title("My first matplotlib sine graph")
# Showing the plot.
plt.show()
