import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-x) * np.sin(x**2) + np.log(x + 2) / (x**2 + 1)

def exact_derivative(x):
    term1 = -np.exp(-x) * np.sin(x ** 2)
    term2 = 2 * np.exp(-x) * np.cos(x ** 2)
    term3 = (x ** 2 + 1 - 2 * x * np.log(x + 2) * (x + 2)) / (np.log(2) * (x + 2) * (x ** 2 + 1) ** 2)
    return term1 + term2 + term3


def finite_difference_forward(x, h):
    return (f(x + h) - f(x)) / h


def finite_difference_backward(x, h):
    return (f(x) - f(x - h)) / h


def finite_difference_central(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


x_range = np.linspace(0, 2, 100)
h_values = [0.1, 0.05, 0.01, 0.005, 0.001]

# Store errors
errors_forward = []
errors_backward = []
errors_central = []

for h in h_values:
    # Calculate the exact derivatives and approximations for the current h
    exact_vals = exact_derivative(x_range)
    forward_vals = finite_difference_forward(x_range, h)
    backward_vals = finite_difference_backward(x_range, h)
    central_vals = finite_difference_central(x_range, h)

    # Calculate errors
    error_forward = np.abs(exact_vals - forward_vals)
    error_backward = np.abs(exact_vals - backward_vals)
    error_central = np.abs(exact_vals - central_vals)

    # Average error for this step size (for plotting after exiting the for loop)
    errors_forward.append(np.mean(error_forward))
    errors_backward.append(np.mean(error_backward))
    errors_central.append(np.mean(error_central))

    # Plotting all three approximations on the same plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, forward_vals, label=f'Forward h={h}', linestyle='-')
    plt.plot(x_range, backward_vals, label=f'Backward h={h}', linestyle='--')
    plt.plot(x_range, central_vals, label=f'Central h={h}', linestyle=':')
    plt.plot(x_range, exact_vals, color='black', linestyle='-', label='Exact Derivative', linewidth=2)

    plt.title(f'Finite Difference Approximations (h={h})', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel("f'(x)", fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plotting errors relative to step size
plt.figure(figsize=(10, 6))
plt.plot(h_values, errors_forward, label='Forward Error', marker='o', linestyle='-')
plt.plot(h_values, errors_backward, label='Backward Error', marker='s', linestyle='--')
plt.plot(h_values, errors_central, label='Central Error', marker='^', linestyle=':')

plt.xscale('log')  # Log scale for x-axis
plt.yscale('log')  # Log scale for y-axis
plt.title('Error vs. Step Size', fontsize=16)
plt.xlabel('Step Size (h)', fontsize=14)
plt.ylabel('Mean Absolute Error', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
