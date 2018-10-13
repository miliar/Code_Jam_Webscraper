#
# IMPORTS
#
from decimal import *
import fileinput

getcontext().prec = 6
data = fileinput.input()
t = int(data[0])

l = 1
for i in range(1, t + 1):
    line = data[l].split()
    d = int(line[0]);
    n = int(line[1]);

    times = []
    for j in range(1, n + 1):
        line = data[l + j].split()
        k = int(line[0])
        s = int(line[1])
        times.append((d - k) / s)

    l = l + n + 1

    h = max(times)
    speed = Decimal(d / h)

    print('Case #{0}: {1:.6f}'.format(i, speed))
