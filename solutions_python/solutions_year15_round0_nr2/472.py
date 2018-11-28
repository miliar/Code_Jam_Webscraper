import sys
stdin = sys.stdin

T = int(stdin.readline())
for icase in range(T):
    D = int(stdin.readline())
    Ps = map(int, stdin.readline().split())
    hist = [0] * (max(Ps)+1)
    for p in Ps:
        hist[p] += 1

    best = 1e9
    for threshold in range(1, max(Ps)+1):
        h = hist[:]
        score = threshold
        for i in reversed(range(len(hist))):
            if i <= threshold:
                break
            score += h[i]
            half = threshold
            h[half] += h[i]
            h[i-half] += h[i]
        best = min(best, score)
        

    print "Case #%d: %d" % (icase+1, best)

