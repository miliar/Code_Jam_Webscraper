import sys

def f(S, K):
    l = len(S)
    for i in range(l + 1 - K):
        if not S[i]:
            for j in range(i, i + K):
                S[j] = not S[j]
            return True
    return False


try:
    T = int(raw_input().strip())
except:
    print 'No input'
    sys.exit()

for i in range(1, T + 1):
    (S, K) = raw_input().strip().split(' ')
    K = int(K)
    S = map(lambda x : x == '+', S)
    c = 0
    while f(S, K):
        c += 1
    if all(S):
        print 'Case #%d: %d' % (i, c)
    else:
        print 'Case #%d: IMPOSSIBLE' % i
