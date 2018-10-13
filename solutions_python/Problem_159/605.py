import sys
stdin = sys.stdin

def solve1(A):
    cur = A[0]
    n = len(A)
    ans = 0
    for i in range(1,n):
        nxt = A[i]
        if nxt < cur:
            ans += cur - nxt
        cur = nxt
    return ans

def solve2(A):
    cur = A[0]
    n = len(A)
    ans = 0; eat = 0
    for i in range(1,n):
        nxt = A[i]
        if cur > nxt:
            eat = max(eat, cur-nxt)
        cur = nxt
    if eat == 0:
        ans = 0
    else:
        for i in range(n-1):
            ans += min(eat,A[i])
    return ans

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        N = stdin.next()
        A = [ int(a) for a in stdin.next().strip().split() ]
        ans1 = solve1(A)
        ans2 = solve2(A)
        # print >>stderr, '--', case
        # if case in [12]:
        #     print >>stderr, A
        #     break
        # print >>stderr, A
        print 'Case #%d:' % case, ans1,ans2

output()
