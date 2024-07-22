import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    a = 1.0
    b = -3.0
    c = 2.0

    temp = a * (time ** 2) + b * time + c
    return temp

def main():
    time_values = np.linspace(0, 10, 50)

    temp_hardcoded = quadratic_model(time_values)

    # Plot the results
    plt.plot(time_values, temp_hardcoded, label='Hard-coded Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation')
    plt.show()

if __name__ == "__main__":
  main()