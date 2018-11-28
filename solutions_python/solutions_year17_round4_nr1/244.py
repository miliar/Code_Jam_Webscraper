import sys
import math

from collections import Counter

def solve_2(groups):
    ans = groups[0]
    ans += (groups[1] + 1) // 2
    return str(ans)

def solve_3(groups):
    pairs = min(groups[1], groups[2])
    rest = max(groups[1], groups[2])  - pairs
    ans = groups[0] + pairs
    ans += (rest + 2) // 3
    return str(ans)
    

def solve_test(inp):
    n, p = map(int, inp.readline().split())
    groups = map(int, inp.readline().split())
    groups = Counter([x % p for x in groups])
    if p == 2:
      return solve_2(groups)

    if p == 3:
      return solve_3(groups)

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()