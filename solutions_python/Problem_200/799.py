#!/usr/bin/python

def ir(): return int(raw_input())
def l2s(a): return''.join(map(str, a)) # list to string

def same_digit(a):
    n = len(a)
    def dfs(b0):
        if len(b0) == n: return b0
        for d in xrange(9, -1, -1):
            b = b0 + [d]
            if len(b) > 1 and not b[-1] >= b[-2]: continue
            if len(b) > 0 and          b[0] == 0: continue
            if not b <= a                       : continue
            rc = dfs(b)
            if rc != None : return rc
    return dfs([])

def less_digit(a): return ['9'] * (len(a) - 1)

def solve():
    a = list(raw_input()); a = map(int, a)
    sd = same_digit(a)
    if sd == None: return l2s(less_digit(a))
    else         : return l2s(sd)

T = ir()
for it in xrange(1, T+1):
    ans = solve()
    print "Case #%d:" % it, ans
