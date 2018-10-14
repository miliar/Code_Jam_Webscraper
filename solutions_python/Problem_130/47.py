def f(N, P):
    if 1 << N == P or N == 1:
        return P
    if P <= 1 << N - 1:
        return 1
    return 2 * f(N - 1, P - (1 << N - 1)) + 1

def g(N, P):
    if 1 << N == P or N == 1:
        return P
    if P >= 1 << N - 1:
        return (1 << N) - 1
    return 2 * g(N - 1, P) - 1

T = input()
for _ in xrange(T):
    [N, P] = map(int, raw_input().split())
    guara = f(N, P) - 1
    could = g(N, P) - 1
    print "Case #%d: %d %d" % (_ + 1, guara, could)
