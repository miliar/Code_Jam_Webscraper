import sys
import math


def getInts():
    return list(map(int, input().split(" ")))

def getFloats():
    return list(map(float, input().split(" ")))


def getNLine( fnc, n ):
    return [ fnc() for y in range(n) ]

def solve(n, u, cores):
    cores.sort()
    cores.append(1)
    for i in range(n):
        temp = (cores[i+1] - cores[i]) *(i+1)
        if temp ==0:
            continue
        elif temp >0 and u>0:
            if temp<=u:
                u-=temp
                for j in range(0,i+1):
                    cores[j] = cores[i+1]
            else:
                for j in range(0,i+1):
                    cores[j] += u/(i+1)
                u=0

    result = 1
    for x in cores:
        result *= x
    return result


T = int(input())
for i in range(T):
    [n, k] = getInts()
    u = float(input())
    cores = getFloats()
    print('Case #{}: {:.6f}'.format(i + 1, solve(n,u,cores)))
