import sys

fp = open(sys.argv[1])
N = int(fp.readline().strip())

def foo(line):
    V, K = line.split(' ')
    K = int(K)
    v = [ 0 if x == '+' else 1 for x in V]
    N = len(v)
    cnt = 0
    if sum(v) == 0:
        return "0"
    if len(v) < K:
        return "IMPOSSIBLE"
    for start in range(N - K + 1):
        if v[start] == 0:
            continue
        cnt += 1
        for pos in range(start, start + K):
            v[pos] = 1 - v[pos]
    if sum(v) == 0:
        return str(cnt)
    return "IMPOSSIBLE"

for case in range(N):
    print 'Case #%d: %s' % (case + 1, foo(fp.readline().strip()))
fp.close()

