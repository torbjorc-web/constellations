# Import internal library
import codecademylib3


# 1
# Import libraries and modules
# Import matplotlib
import matplotlib.pyplot as plt

# Import 3D visualization library
from mpl_toolkits.mplot3d import Axes3D


# 2
# View given x,y,z coordinates
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]


# 3
# Create a figure
fig_2d = plt.figure()

# Add your subplot
ax2d = fig_2d.add_subplot(1, 1, 1)

# Create a scatter plot
ax2d.scatter(x, y)
plt.show()


# 4
# Create a figure
fig_3d = plt.figure()

# Add your subplot
ax3d = fig_3d.add_subplot(1, 1, 1, projection='3d')

# Create a scatter plot
ax3d.scatter(x, y, z)
plt.show()


# Challenge
# Create a night sky scatter plot
# Create a figure
fig_2d_night = plt.figure()

# Add your subplot
ax2d_night = fig_2d_night.add_subplot(1, 1, 1)

# Change color of plot background
ax2d_night.set_facecolor('black')

# Create a scatter plot with black background
ax2d_night.scatter(x, y, color='white')
plt.show()


# Create a figure
fig_3d_night = plt.figure()

# Add your subplot
ax3d_night = fig_3d_night.add_subplot(1, 1, 1, projection='3d')

# Change color of plot background
ax3d_night.set_facecolor('black')

# Create a scatter plot with black background
ax3d_night.scatter(x, y, z, color='white')
plt.show()


# Create a figure
fig_3d_night_blue = plt.figure()

# Add your subplot
ax3d_night_blue = fig_3d_night_blue.add_subplot(1, 1, 1, projection='3d')

# Change color of plot background
ax3d_night_blue.set_facecolor('midnightblue')

# Create a scatter plot with black background
ax3d_night_blue.scatter(x, y, z, color='yellow')
plt.show()
