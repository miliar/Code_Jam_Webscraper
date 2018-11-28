T = int(raw_input())

for j in range(T):
    cps = 2.0
    C, F, X = map(float, raw_input().split(' '))
    best = X / cps
    cost = 0
    while True:
        next = cost + C / cps + X / (cps + F)
        if (next < best):
            best = next
            cost += C / cps
            cps += F
        else:
            break
    print "Case #{}: {}".format(j+1, best)