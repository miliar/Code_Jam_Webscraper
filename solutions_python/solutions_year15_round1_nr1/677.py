import sys
import math
import numpy as np
from pprint import pprint

numTests = int(sys.stdin.readline().rstrip("\n"))

def eat1(values):
    if(len(values) <= 1):
        return 0

    prev = values[0]
    diff = 0
    for i in xrange(1,len(values)):
        if(prev > values[i]):
            diff += abs((values[i] - prev))
        prev = values[i]
    return diff

def eat2(values):
    prev = values[0]
    rate = 0
    for i in xrange(1,len(values)):
        if( prev > values[i]):
            diff = abs(values[i] - prev)
            rate = max(rate,diff)
        prev = values[i]

    count = 0
    prev = values[0]
    for i in xrange(1,len(values)):
        if( prev > values[i]):
            count += min(rate,prev)
        else:
            count += min(rate,prev)

        prev = values[i]

    return count


for test_num in xrange(numTests):
    N = int(sys.stdin.readline().rstrip("\n"))
    values = map(int,sys.stdin.readline().rstrip("\n").split(" "))

    y = eat1(values)
    z = eat2(values)
    print("Case #"+ str(test_num + 1) + ": " + str(y) +  " " + str(z))
