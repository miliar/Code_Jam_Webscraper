
k = int(raw_input())

for i in range(k):
    D, N = map(int, raw_input().split())
    max_t = 0
    min_v = 0
    for j in range(N):
        s, v = map(int, raw_input().split())
        t = float(D-s)/v
        if t > max_t:
            max_t = t
    print "Case #{0}: {1:.6f}".format(i+1, D/max_t)

    