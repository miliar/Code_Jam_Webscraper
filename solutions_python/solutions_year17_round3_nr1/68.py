import sys
import math


def solve_test(inp):
    n, k = map(int, inp.readline().split())
    pancakes = []
    for i in range(n):
      r, h = map(int, inp.readline().split())
      pancakes.append((r, h, 2 * r * h, r ** 2))

    taken = []
    pancakes.sort(key = lambda x : (x[2], x[3]))
    taken = pancakes[-k:] 
    pancakes = pancakes[:-k]
    bottom = max([x[3] for x in taken])
    taken.sort(key= lambda x : x[2])
    for p in pancakes:
      if p[2] + p[3] - bottom > taken[0][2]:
        taken[0] = p
        bottom = p[3]
    
        
    #pancakes.sort(key = lambda x : x[2])
    #if k > 1:
    #  taken += pancakes[-k+1:]
    result = sum(x[2] for x in taken) + bottom
   
    return '%.9f' % (math.pi * result) 

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()