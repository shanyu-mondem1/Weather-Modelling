import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def quad_eq(time,a,b,c):
  temp = a * (time ** 2) + b * time + c
  return temp

file = '/content/sample_data/MultiValueSet.csv'
df = pd.read_csv(file)
print(df)
row = int(input('\nEnter row number you want to use: '))

row_values = df.loc[row].values.flatten().tolist()

time_values = np.linspace(int(row_values[0]),int(row_values[1]),int(row_values[2]))

temp_hardcoded_val = quad_eq(time_values,row_values[3],row_values[4],row_values[5])

plt.plot(time_values, temp_hardcoded_val, label='Hard-coded Coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('Weather Modeling with Quadratic Equation')
plt.show()
