def Snapper(N, K):
    if K == 0:
        return "OFF"
    if (K + 1) % (2 ** N) == 0: 
        return "ON"
    return "OFF"

T = input()
for i in range(0, T):
    N, K = raw_input().split()
    N = int(N)
    K = int(K)
    print "Case #%s: %s" % (i + 1, Snapper(N, K))
