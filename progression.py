import numpy as np
import matplotlib.pyplot as plt
from deckarray import deck
x = []
y = []
for xa in deck:
    x.append(xa[1])
    yp = 0
    if len(xa[2])>0:
        if xa[2][-1] == "jlpt-n1":
            yp = 1
        elif xa[2][-1] == "jlpt-n2":
            yp = 2
        elif xa[2][-1] == "jlpt-n3":
            yp = 3
        elif xa[2][-1] == "jlpt-n4":
            yp = 4
        elif xa[2][-1] == "jlpt-n5":
            yp = 5
    else:
        yp = -1
    y.append(yp)

print(x)
print(y)
print(len(x))
print(len(y))
# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('Card #')
# naming the y axis
plt.ylabel('JLPT Level')
plt.ylim((-1,6))
# giving a title to my graph
plt.title('Kaishi 1.5k progression mapped to JLPT Level')

# function to show the plot
plt.show()