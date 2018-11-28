import math


def isTidy(num):
    last = 9
    for x in reversed(str(num)):
        if int(x) <= last:
            last = int(x)
        else:
            return False
    return True

def linearSearch(num):
    for i in xrange(num):
        if isTidy(num-i):
            return num-i

t = int(input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = linearSearch(int(input()))
    print("Case #{}: {}".format(i, n))
