
def solve(t):
    X = map(int, raw_input())

    for i in xrange(len(X)-1, -1, -1):
        if i+1 < len(X) and X[i] > X[i+1]:
            X[i] = X[i]-1
            for j in xrange(i+1, len(X)):
                X[j] = 9

    ans = int(''.join(map(str, X)))
    print 'Case #%d: %d' % (t, ans)

T = input()
for i in xrange(T):
    solve(i+1)
