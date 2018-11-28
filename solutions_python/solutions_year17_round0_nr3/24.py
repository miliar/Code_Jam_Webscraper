import sys

def next_line():
    return input_file.readline().rstrip()

table = {}
def min_max(N, K):
    assert(K >= 0)
    if K == 0:
        return N
    elif N == K:
        return 0
    if (N, K) not in table:
        Np, Kp = N-1, K-1
        L, R = Np/2, Np-Np/2
        i = Kp/2
        table[(N, K)] = max(min_max(L, i), min_max(R, Kp-i))
        #table[(N, K)] = min(max(min_max(L, i), min_max(R, Kp-i))
        #                    for i in xrange(max(0, Kp-R), min(L, Kp) + 1))
    return table[(N, K)]

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    N, K = map(int, next_line().split())
    S = min_max(N, K-1)
    Sp = S - 1
    print Sp-Sp/2, Sp/2
    #print S
