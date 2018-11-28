from sys import stdin
def solve():
    read_ints = lambda: map(int, stdin.readline().split())
    n = int(stdin.readline())
    a = read_ints()
    ans = 0
    for i, x in enumerate(a):
        ans += min(sum(1 for j in xrange(i) if a[j] > x), sum(1 for j in xrange(i+1, n) if a[j] > x))
    return ans
T = int(raw_input())
for t in xrange(T):
    print "Case #%d: %d" % (t+1, solve())
