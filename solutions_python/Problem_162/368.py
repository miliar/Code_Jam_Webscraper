from collections import deque

def rev(x):
    def rev(x, res):
        return res if x == 0 else rev(x / 10, x % 10 + res * 10)
    res = rev(x / 10, x % 10)
    #print "\t", (x, res)
    return res

def solve(n):
    v = set()
    s = deque()
    s.append((1, 1))
    v.add(1)
    while s:
        x, res = s.popleft()
        #print x, res
        if x == n: return res
        for i in [x+1, rev(x)]:
            if i not in v:
                s.append((i, res+1))
                v.add(i)

T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    print "Case #%d: %d" % (t, solve(N))

