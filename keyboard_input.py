import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    print('Enter the coefficients (a,b,c): ')
    a,b,c = input().split()

    temp = float(a) * (time ** 2) + float(b) * time + float(c)
    return temp

def main():
    print('Enter the (lower bound, upper bound, no of values): ')
    ub, lb, nv = input().split()
    time_values = np.linspace(int(ub), int(lb), int(nv))

    temp_hardcoded = quadratic_model(time_values)

    # Plot the results
    plt.plot(time_values, temp_hardcoded, label='Hard-coded Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation')
    plt.show()
    # print(time_values)

if __name__ == "__main__":
  main()