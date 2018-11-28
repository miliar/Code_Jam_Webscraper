from sys import stdin
#import sympy
def f(a,y):
    return (1/4) * ((4 * a**2-4*a + 8*y + 1)**(1/2) - 2*a + 1)
def g(n,r):
    return n*(2*n + 2*r -1)

def solve(r,t):
    x0 = int(f(r,t)) 
    while g(x0, r) < t:
        x0 += 1
    while g(x0, r) > t:
        x0 -= 1
    return x0
T = int(stdin.readline())

for testcase in range(1,1+T):
    r,t = [float(s) for s in stdin.readline().split()]
    print("Case #%d: %d" % (testcase, (solve(r,t))))
