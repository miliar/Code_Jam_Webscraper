import sys

def isgood(n):
    c = 9
    while n > 0:
        if n % 10 > c:
            return False
        c = n % 10
        n = n // 10
    return True

def run(N):
    if isgood(N): return N
    b = 0

    for i in range(20):
        k = (N // (10**i)) * (10**i) - 1
        if isgood(k):
            b = max(b, k)
    return b


f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    N = f.readline().strip()
    ans = run(int(N))
    print 'Case #%d: %s' % (case, ans)
