#  Find (3+ sqrt(5))**N mod 1000.

from math import *

def factorial(N):
    if N == 0: return 1
    i = 1
    for j in range(1,N+1):
        i *= j
    return i
def binom(n, k):
    if not 0 <= k <= n:
        return 0
    if k == 0 or k == n:
        return 1
    # calculate n!/k! as one product, avoiding factors that 
    # just get canceled
    P = k+1
    for i in xrange(k+2, n+1):
        P *= i
    # if you are paranoid:
    # C, rem = divmod(P, factorial(n-k))
    # assert rem == 0
    # return C
    return P//factorial(n-k)

def sol(n):
    k = 0
    ans = 0
    while 2*k<= n:
        #print k
        #print ans
        ans += ((3**(n-2*k))*(5**k)*binom(n,2*k))%1000
        k += 1
    ans *= 2
    ans -= 1
    ans = ans%1000
    return ans

def h(N):
    return f(sol(N))
def f(z):
    if z < 10:
        s = '00'+str(z)
    if z >= 10 and z < 100:
        s = '0'+str(z)
    if z >= 100:
        s = str(z)
    return s

inn = open('input.txt', 'r')
def getz():
    global inn
    return inn.readline().strip()

T = int(getz())

for i in range(T):
    N = int(getz())
    print "%s%d%s%s" % ("Case #",i+1,": ",h(N))
