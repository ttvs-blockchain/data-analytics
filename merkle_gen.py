import math
import matplotlib.pyplot as plt
from typing import List

data = [
    [13171711, 10288033, 12009811],
    [85423012, 87307297, 87676900],
    [425821965, 424517555, 460783653],
    [2916612265, 2807776584, 2791181068],
    [331096501189, 339667987552, 370665918466],
]

def process_data(data: List[List[int]])-> List[int]:
    avg_data: List[int] = []
    for i in range(len(data)):
        avg_data.append(int(math.log2(sum(data[i]) // len(data[i]))))
    return avg_data

processed_data = process_data(data)
print(processed_data)

fig = plt.figure()
x_axis_values = ['2^5', '2^10', '2^15', '2^20', '2^25']
y_axis_values = processed_data
plt.bar(x_axis_values, y_axis_values)
plt.title('Merkle Tree Generation Time')
plt.xlabel('Test Size')
plt.ylabel('Time(ns) in log2')
plt.show()