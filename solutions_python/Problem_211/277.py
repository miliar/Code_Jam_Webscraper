def product(l):
    p = 1
    for i in l:
        p *= i
    return p

t = int(input())  # read a line with a single integer
for az in range(1, t+1 ):
    n, k = [int(e) for e in input().split(" ")]   
    u = float(input())
    Probas = [float(e) for e in input().split(" ")]
    Probas.append(1)
    Probas.sort(key=lambda l:l)
    s = 0
    i = 1
    while i<n and s+(Probas[i]-Probas[i-1])*i < u :
        s = s+(Probas[i]-Probas[i-1])*i
        for k in range(i):
            Probas[k] = Probas[i]
        i += 1
    for k in range(i):
        Probas[k] += (u-s)/i
    M = min(product(Probas),1)
        

    print("Case #{}: {}".format(az, M) )