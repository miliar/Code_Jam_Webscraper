from math import pi
from itertools import combinations

fin = open('A.in', 'r')
fout = open('A.out', 'w')


def calc_area(p):
    # sort p by smallest radius
    p = sorted(list(p))
    # add surface area of 
    ans = sarea(p[0])
    hidden = area(p[0][0])
    for i in range(1, len(p)):
        ans += sarea(p[i]) - hidden 
        hidden = area(p[i][0])
    return ans

def area(R):
    return pi * R**2

def sarea(pair):
    R, H = pair
    return pi * R**2 + 2 * pi * R * H

T = int(fin.readline())
for t in range(1, T+1):
    N, K = map(int, fin.readline().split())
    pancakes = []
    for i in range(N):
        R, H = map(int, fin.readline().split())
        pancakes.append((R, H))
    P = list(combinations(pancakes, K))
    syrup = map(calc_area, P)
    ans = max(syrup)
    fout.write('Case #' + str(t) + ': %.9f\n' % ans) 
