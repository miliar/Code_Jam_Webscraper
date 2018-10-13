T = int(raw_input())

for t in range(T):
    f = 0

    S, K = raw_input().strip().split(' ')
    S = list(S)
    l = len(S)
    K = int(K)

    flips = 0
    impossible = False
    for y in range(l):

        if S[y] is '-':
            if y > (l - K):
                impossible = True
            else:
                flips += 1
                for x in range(K):
                    if S[x + y] is '-':
                        S[x + y] = '+'
                    else:
                        S[x + y] = '-'

    if impossible:
        flips = "IMPOSSIBLE"

    print "Case #%d: %s" % (t + 1, flips)
