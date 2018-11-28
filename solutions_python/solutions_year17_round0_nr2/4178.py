import numpy as np
from collections import Counter
from math import *

def is_tidy(n):
    s = str(n)
    for i in range(0, len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return int(s[0:i] + str(int(s[i])-1) + '9'*(len(s)-(i+1)))

f = file('input2.in')
out = open('output2.txt', 'w+')
T = int(f.readline())
for i in range(1, T+1):
    N = int(f.readline())
    while True:
        n = is_tidy(N)
        if n is None:
            break
        else:
            N = n

    line = "Case #" + str(i) + ": " + str(N)
    print(line)
    out.write(line + "\n")
f.close()
out.close()