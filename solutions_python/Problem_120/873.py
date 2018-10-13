
import sys, math
getl = lambda : sys.stdin.readline().strip()

def area(r, i):
    return math.pi * (2*r + 1 + 4*i)

def volume(r, n):
    return (n+1)*(2*r + 1) + 2*n*(n+1)

cases = range(int(getl()))
for case in cases:
    r,t = [int(x) for x in getl().split()]

    result0 = int((-(2+2*r+1) + math.sqrt((2+2*r+1)**2 - 8*(-t+2*r+1))) / 4)
    result1 = int((-(2+2*r+1) - math.sqrt((2+2*r+1)**2 - 8*(-t+2*r+1))) / 4)
    result = max(list(filter(lambda x: volume(r, x) <= t, [result0, result1])))

    print('Case #%d: %d' %(case+1, result+1))
