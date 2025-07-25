import matplotlib.pyplot as plt
import numpy as np

# Read data from file
with open("sosound.txt", "r") as f:
    lines = f.readlines()

# Extract and clean data
x_line = lines[0].split(":")[1].strip().split()
y_line = lines[1].split(":")[1].strip().split()

# Convert to numpy arrays
x = np.array([float(val) * 1e-3 for val in x_line])  # 1/f in seconds
y = np.array([float(val) for val in y_line])         # L in meters

# Line of best fit
coeffs = np.polyfit(x, y, 1)
fit_fn = np.poly1d(coeffs)

# Plotting
plt.scatter(x, y, label="Data points")
plt.plot(x, fit_fn(x), color="red", label=f"Best fit: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
plt.xlabel("1/f (s)")
plt.ylabel("L (m)")
plt.title("Line of Best Fit for Speed of Sound")
plt.legend()
plt.grid(True)
plt.show()

# Print equation
print(f"Equation: L = {coeffs[0]:.4f} * (1/f) + {coeffs[1]:.4f}")
