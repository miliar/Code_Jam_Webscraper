T = int(input())
for i in range(T):
    Smax, Ss = input().split()
    Ss = map(int, list(Ss))
    up = 0
    extras = 0
    for j, ss in enumerate(Ss):
        if up < j:
            extras += j - up
            up = j
        up += ss
    print("Case #%d: %d" % (i+1, extras))
