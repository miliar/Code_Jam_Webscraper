import sys


def solve_test(inp):
    pancakes, k = inp.readline().split()
    pancakes = list(pancakes)
    k = int(k)
    n = len(pancakes)
    flips = 0
    for i in range(n-k+1):
      if pancakes[i] == '-':
        flips += 1
        for j in range(i, i+k):
          pancakes[j] = '-' if pancakes[j] == '+' else '+'
    if any(x == '-' for x in pancakes[-k:]):
      return 'IMPOSSIBLE'  
    return str(flips) 

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()