from decimal import *
import math

output = []
with open('B-large.in.txt') as file:
    T = int(file.readline().split()[0])
    for i in xrange(T):
        c, f, x = [float(x) for x in file.readline().split()]
        rate = 2; t = 0
        while (x - c) * (rate + f) > x * rate:
            t += c / rate
            rate = rate + f
        t += x / rate
        output += ['Case #' + str(i + 1) + ': ' + str(t)]

with open('output.txt', 'w') as f:
    f.write('\n'.join(output))