import fileinput
import math
import sys

def val(r, n):
    return (2*r + 1)*(n) + 2*(n*n - n)

def bin_search(r, t, i, j):
    if i == j or i+1 == j:
        return i
    mid = (i+j)/2
    #print i, j
    v = val(r, mid)
    if v == t:
        return mid
    elif val(r, mid) > t:
        return bin_search(r, t, i, mid)
    else:
        return bin_search(r, t, mid, j)
    

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in xrange(T):
        r, t = map(int, sys.stdin.readline().split(' '))
        #ans = math.floor(((-2.0*r + 1.0) + math.sqrt((4.0*r*r - 4.0*r + 1.0) + 8.0*t))/4.0)
        ans = bin_search(r, t, 0, t)
        print "Case #{}: {}".format(i+1, int(ans))
