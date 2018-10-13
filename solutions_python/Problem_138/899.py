def war(N, K):
    score = 0
    for n in N:
        if n > K[-1]:
            score += 1
            K.pop(0)
        else:
            i = 0
            while K[i] < n:
                i += 1
            K.pop(i)
    return score


def d_war(N, K):
    score = 0
    while N:
        if N[-1] > K[-1]:
            score += 1
            N.pop()
            K.pop()
        else:
            N.pop(0)
            K.pop()
    return score


for i in xrange(input()):
    input()
    N = map(float, raw_input().split())
    K = map(float, raw_input().split())

    print "Case #%d: %d %d" % (i + 1,
                               d_war(sorted(N), sorted(K)),
                               war(sorted(N, reverse=True), sorted(K)))
