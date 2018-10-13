T = int(input())

for t in range(T):
    C, F, X = map(float, input().split())
    time = 0
    rate = 2

    ttc = X/rate
    ttn = C/rate
    nttc = X/(rate+F)
    while ttc > ttn + nttc:
        time += ttn
        rate += F
        ttc = X/rate
        ttn = C/rate
        nttc = X/(rate+F)

    time += ttc
    print('Case #{}: {:.7f}'.format(t+1, time))

    
