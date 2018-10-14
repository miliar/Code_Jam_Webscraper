from math import ceil
from math import floor

T = int(raw_input(""))

for o in range(1, T+1):
    N, K = raw_input("").split(" ")

    K = int(K)
    i = 0
    N = [x == "+" for x in N]
    count = 0
    while i + K <= len(N):
        if not N[i]:
            count += 1
            for j in range(i, i+K):
                N[j] = not N[j]

        i += 1

    if sum([0 if x else 1 for x in N]) > 0:
        print "Case #%d: IMPOSSIBLE" % (o)
    else:
        print "Case #%d: %d" % (o, count)
