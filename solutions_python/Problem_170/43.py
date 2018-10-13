import copy

ans = 2333333333333333333333

def do_solve(eng, fre, strs, magic, n):
    ee = set([])
    ff = set([])
    cnt = 0
    for i in xrange(n):
        if (magic & (1 << i)):
            ee |= set(strs[i])
        else:
            ff |= set(strs[i])
        cnt += 1
    return len((eng | ee) & (fre | ff))

def solve():
    n = int(raw_input())
    eng = set(raw_input().split())
    fre = set(raw_input().split())
    strs = [raw_input().split() for i in xrange(n - 2)]
    ans = 2333333333333333333333
    
    for i in xrange(1 << (n - 2)):
        ans = min(ans, do_solve(eng, fre, strs, i, n - 2))
    print ans
    
T = int(raw_input())
for cas in xrange(T):
    print "Case #%d: " % (cas + 1),
    solve()
