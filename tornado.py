import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
for line in open('data.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(int(lines[1]))

plt.title("Yearly Tornado Trends in Arkansas 1950-2022")
plt.xlabel('Year')
plt.ylabel('Number of Tornados')
plt.yticks(np.arange(0, 200, 25))
plt.xticks(np.arange(0, 2022, 10))
plt.plot(x, y, marker = 'o', c = 'g')
