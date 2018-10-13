#!/usr/bin/python
import math
t = int(raw_input())  # read a line with a single integer


def minmax(n,k):
    if k <= 1:
        return (int(math.ceil((n-1)/2.0)),int(math.floor((n-1)/2.0)))
    else:
    #    lk=math.floor(math.log(k,2))
        if k%2 == 0:
            return (minmax(math.ceil((n-1)/2.0),(k+1)/2))
        else:
            return (minmax(math.floor((n-1)/2.0),k/2))



for i in range (1,t+1):
    n, m = [int(s) for s in raw_input().split(" ")]
    a , b = minmax(n,m)
    print("Case #{}: {} {}".format(i, a, b))
