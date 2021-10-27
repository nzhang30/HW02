import matplotlib.pyplot as plt

import csv

file = open('population_china.csv')
r = csv.reader(file)
data = list(r)

year = []
population = []

# year
x1 = data[1][0]
year.append(x1)
x2 = data[2][0]
year.append(x2)
x3 = data[3][0]
year.append(x3)
x4 = data[4][0]
year.append(x4)
x5 = data[5][0]
year.append(x5)
x6 = data[6][0]
year.append(x6)
x7 = data[7][0]
year.append(x7)
x8 = data[8][0]
year.append(x8)
x9 = data[9][0]
year.append(x9)
x10 = data[10][0]
year.append(x10)
x11 = data[11][0]
year.append(x11)
x12 = data[12][0]
year.append(x12)


# population
y1 = int(data[1][1])
population.append(y1)
y2 = int(data[2][1])
population.append(y2)
y3 = int(data[3][1])
population.append(y3)
y4 = int(data[4][1])
population.append(y4)
y5 = int(data[5][1])
population.append(y5)
y6 = int(data[6][1])
population.append(y6)
y7 = int(data[7][1])
population.append(y7)
y8 = int(data[8][1])
population.append(y8)
y9 = int(data[9][1])
population.append(y9)
y10 = int(data[10][1])
population.append(y10)
y11 = int(data[11][1])
population.append(y11)
y12 = int(data[12][1])
population.append(y12)


# plot bar graph
plt.plot(year, population, color = 'b')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Population', fontweight='bold')
plt.legend()
plt.savefig('population_china.jpg')
plt.show()


import csv

file = open('UN_Data.csv')
r = csv.reader(file)
data = list(r)

countries = []
density = []

# countries
x1 = data[90][1]
countries.append(x1)
x2 = data[119][1]
countries.append(x2)
x3 = data[148][1]
countries.append(x3)
x4 = data[177][1]
countries.append(x4)

    
# density
y1 = int(float(data[90][4]))
density.append(y1)
y2 = int(float(data[119][4]))
density.append(y2)
y3 = int(float(data[148][4]))
density.append(y3)
y4 = int(float(data[177][4]))
density.append(y1)


# plot bar graph
plt.bar(countries, density, color = 'b')
plt.xlabel('Country', fontweight='bold')
plt.ylabel('Population Density', fontweight='bold')
plt.legend()
plt.savefig('Population_density_Africa.jpg')
plt.show()