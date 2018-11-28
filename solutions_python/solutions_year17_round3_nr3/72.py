import sys


def solve_test(inp):
    n, k = map(int, inp.readline().split())
    u = float(inp.readline())
    p = [float(x) for x in inp.readline().split()]
    p.sort()
    p += [1]
    n = 1
    while n < len(p):
      #print(p, u)
      delta = p[n] - p[n-1] 
      toadd = min(u, delta * n) 
      add = toadd / n
      for i in range(n):
        p[i] += add
      u -= toadd
      n += 1
    prod = 1
    for x in p:
      prod *= x
    return str(prod) 

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()