import numpy as np
import matplotlib.pyplot as plt
import random
import math
def height_formula (x) :
    # we use 1 - (320!/320^k * (320-k)!)
    sorat = math.factorial(320)
    maj1 = 320 ** x
    maj2 = math.factorial(320 - x)
    comp = sorat / (maj1 * maj2)
    return (1 - comp)
def height_practical(number) :
    randclass = [0] * number
    prob = []
    for j in range (0 , 100) :
        for i in range (0 , number) :
            randclass[i] = random.randint(1, 320)
        flag = 0
        # using set() + len()
        # to check all unique list elements
        flag = len(set(randclass)) == len(randclass)
        if (flag):
            prob.append(0)
        else :
            prob.append(1)
    return (sum(prob)/100)
x = np.arange(1,320)
y = [height_formula(x) for x in range (1,320)]
#first number that give probability upper then 0.5 is our ans
mark = next(x for x, val in enumerate(y) if val > 0.5)
y1 = [height_practical(x) for x in range (1,320)]
plt.figure()
plt.subplot(1,2,1)
plt.plot (x ,y ,'g')
# we mark our ans for 0.5 probability in plot
plt.plot(x[mark], y[mark], 'ro')
plt.annotate ('(%d, %.1f)' % (x[mark],y[mark]),xy=(x[mark],y[mark]), textcoords='data')
print(f'we need more then {mark} people for Probability grater then 0.5')
plt.title ('height_formula')
plt.xlabel ('Number of people')
plt.ylabel ('Probability of a pair')
plt.subplot(1,2,2)
plt.plot (x, y1, 'bo')
plt.title ('height_practical')
plt.xlabel ('Number of people')
plt.ylabel ('Probability of a pair')
plt.show()