# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:56:13 2023

@author: Jermaine Cort
"""

import time
import numpy as np
import matplotlib.pyplot as plt

# Start measuring time
start_time = time.time()

# Initialize an empty list to store the array
my_array = []

# Use a for loop to populate the array
for i in range(10):
    my_array.append(i)

# Print the resulting array
print("Array:", my_array)

# Calculate and print the computational time
end_time = time.time()
elapsed_time = end_time - start_time
print("Computational Time:", elapsed_time, "seconds")

# Start measuring time
start_time2 = time.time()

# Initialize variables
my_array = []
count = 0

# Use a while loop to populate the array
while count < 10:
    my_array.append(count)
    count += 1

# Print the resulting array
print("Array:", my_array)

# Check if the 10th number is 9 and print the message accordingly
if my_array[-1] == 9:
    print("The 10th number in the while array is 9")

# Calculate and print the computational time
end_time2 = time.time()
elapsed_time = end_time2 - start_time2
print("Computational Time:", elapsed_time, "seconds")


def calculate_cosine(xmin, xmax, nx):
    """
    Calculate the cosine function over the specified x-range.

    Args:
        xmin (float): The minimum value of x.
        xmax (float): The maximum value of x.
        nx (int): The number of points in the x-array.

    Returns:
        x (numpy.ndarray): The x-array.
        cosine_values (numpy.ndarray): The corresponding cosine values.
    """
    x = np.linspace(xmin, xmax, nx)
    cosine_values = np.cos(x)
    return x, cosine_values

# Example usage:
xmin = 0
xmax = 2 * np.pi
nx = 100
x, cosine_values = calculate_cosine(xmin, xmax, nx)
print("x-array:", x)
print("Cosine values:", cosine_values)

def calculate_cosine(xmin, xmax, nx, amplitude):
    x = np.linspace(xmin, xmax, nx)
    cosine_values = amplitude * np.cos(x)
    return x, cosine_values

# Define parameters
xmin = 0
xmax = 2 * np.pi
nx = 100

# Different amplitudes to iterate over
amplitudes = [1.0, 2.0, 0.5]

# Create a figure and axis for the plot
plt.figure(figsize=(8, 6))

# Loop through amplitudes and plot each cosine curve
for amplitude in amplitudes:
    x, cosine_values = calculate_cosine(xmin, xmax, nx, amplitude)
    plt.plot(x, cosine_values, label=f'Amplitude {amplitude}')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Cosine(x)')
plt.legend()

# Show the plot
plt.show()

def calculate_cosine(xmin, xmax, nx, amplitude):
    x = np.linspace(xmin, xmax, nx)
    cosine_values = amplitude * np.cos(x)
    return x, cosine_values

def main():
    # Define parameters
    xmin = 0
    xmax = 2 * np.pi
    nx = 100

    # Different amplitudes to iterate over
    amplitudes = [1.0, 2.0, 0.5]

    # Create a figure and axis for the plot
    plt.figure(figsize=(8, 6))

    # Loop through amplitudes and plot each cosine curve
    for amplitude in amplitudes:
        x, cosine_values = calculate_cosine(xmin, xmax, nx, amplitude)
        plt.plot(x, cosine_values, label=f'Amplitude {amplitude}')

    # Add labels and legend
    plt.xlabel('x')
    plt.ylabel('Cosine(x)')
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
