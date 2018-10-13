from itertools import *

def check(x, y):
    if calc(x) == calc(y):
        return max(sum(x), sum(y))
    else: return -1

def calc(x):
    ret = 0
    for c in x:
        ret ^= c
    return ret

T = int(raw_input())

for t in range(T):
    N = int(raw_input())

    C = map(int, raw_input().split())
    #print C

    ans = -1
    for i in range(1, 2**(N-1)):
        #print i
        x = [C[j] for j in range(N) if i & 2**j]
        y = [C[j] for j in range(N) if not (i & 2**j)]
        #print x, y
        ans = max(ans, check(x, y))
    
    if ans == -1:
        print "Case #%d: NO" % (t+1)
        
    else:
        print "Case #%d: %d" % (t+1, ans)
        