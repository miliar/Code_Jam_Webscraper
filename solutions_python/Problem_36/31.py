import sys, re

def lin(): return sys.stdin.readline()

pat = "welcome to code jam"
Y = len(pat)
x = 0
s = ""
nt = []

def times(x, y):
    global X,Y,s, nt
    if x>=X: return 0
    if y==Y: return 1
    if nt[x][y]>=0: return nt[x][y]
    assert 0<=x<X and 0<=y<Y
    ans = 0
    for i in range(x, X):
        if s[i] == pat[y]:
            ans = (ans + times(i+1, y+1)) % 10000
    nt[x][y] = ans
    return ans

N = int(lin())
for casenum in range(N):
    s = lin()
    X = len(s)
    nt = [ [-1 for j in range(Y)] for i in range(X) ]
    ans = times(0,0)
    print "Case #%d: %s" % (casenum+1, str(ans).rjust(4,'0'))



