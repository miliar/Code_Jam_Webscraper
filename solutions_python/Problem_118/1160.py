# Python 2.7

import sys
import math

def fair(number):
    s = str(number)
    return s == s[::-1]
    

f = sys.stdin

count = int(f.readline())

for index in range(1, count+1):
    dim = f.readline().strip()
    [start, stop] = map(int, dim.split(" "))

    count = 0
    for i in range(start, stop+1):      # stop included
        if fair(i):
            root = int(math.sqrt(i))
            if root**2 == i:
                if fair(root):
                    count += 1
                    #print("{} = {}^2".format(i, root))
    print("Case #{}: {}".format(index, count))