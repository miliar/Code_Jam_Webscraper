N = int(input())

for i in range(N):
    data, k = input().split(' ')
    k = int(k)
    data = list(data)
    for p in range(len(data)):
        if data[p] == '-':
            data[p] = False
        else:
            data[p] = True

    nflips = 0
    for p in range(len(data)):
        if data[p] == False:
            if p+k > len(data):
                nflips = "IMPOSSIBLE"
                break
            for p_ in range(k):
                data[p+p_] = not(data[p+p_])
            nflips += 1

    print(("Case #%d: " % (i+1))+str(nflips))
