import sys

def run(N, K):
    t = 0
    while 2*t + 1 < K:
        t = 2*t + 1
    r = K - t
    m = (N - t) // (t+1)
    r2 = (N - t) % (t+1)
    if r2 >= r:
        m = m+1
    return '%d %d' % (m//2, (m-1)//2)

f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    N,K = f.readline().strip().split()
    ans = run(int(N), int(K))
    print 'Case #%d: %s' % (case, ans)
