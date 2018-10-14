import itertools
import math

def surface_area(r, h):
    return 3.14159 * r * r + 2 * 3.14159 * r * h

def stack_area(stk):
    stk = sorted(stk)
    area = 0
    last_face = 0
    for s in stk:
        r,h = s
        area += 2 * math.pi * r * h 
        area += math.pi * r * r
        area -= last_face
        last_face = math.pi * r * r

    return area

def solve(n, k, cakes): 
    perms = itertools.combinations(cakes, k)
    
    maxn = 0   
    for p in perms:
        k = stack_area(p)
        if k > maxn:
            maxn = k #stack_area(p)
    
    #print('[{0}, {1}, {2}]'.format(n, k, cakes))
    return maxn 

for i in range(0, int(input())):
    n,k = list(map(int, input().split())) 
    cakes = []
    for j in range(0, n):
        cakes.append(list(map(int, input().split())))

    print("Case #{0}: {1:.16f}".format(i + 1, solve(n, k, cakes)))


