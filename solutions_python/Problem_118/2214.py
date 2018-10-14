fs = [1, 4, 9, 121, 484]

T = int(raw_input())
for t in range(T):
    a, b = [int(i) for i in raw_input().split()]
    n = 0
    for f in fs:
        if a <= f <= b:
            n += 1
    print "Case #{0}: {1}".format(t+1, n)
