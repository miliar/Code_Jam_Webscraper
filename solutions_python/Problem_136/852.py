import sys
input = file(sys.argv[1])

T = int(input.readline())

def s(P, C, F, X):
    ans1 = X/P
    t = 0.0
    while True:
        t += C/P
        P += F
        ans = t + X/P
        if ans > ans1:
            return ans1
        ans1 = ans
    
def solve():
    C, F, X = map(float,input.readline().split())
    return s(2.0, C, F, X)

for t in range(T):
    print 'Case #%s: %s' % (t+1,solve())
