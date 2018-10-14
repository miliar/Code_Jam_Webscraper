T = int(input())

for i in range(T):
    C, F, X = map(float, input().split())
    cps = 2
    time = C/cps
    while (X-C)/cps > X/(cps+F):
        cps += F
        time += C/cps
    time += (X-C)/cps
    print('Case #%d: %.7f' % (i+1, time))
