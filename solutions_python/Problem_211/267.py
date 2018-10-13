def product(l):
    p = 1
    for i in l:
        p *= i
    return p

t = int(raw_input())  # read a line with a single integer
for z in range(1, t+1 ):
    n, k = [int(e) for e in raw_input().split(" ")]   
    u = float(raw_input())
    P = [float(e) for e in raw_input().split(" ")]
    P.append(1)
    P.sort(key=lambda l:l)
    s = 0
    i = 1
    while i<n and s+(P[i]-P[i-1])*i < u :
        s = s+(P[i]-P[i-1])*i
        for k in range(0, i):
            P[k] = P[i]
        i = i+1
    for k in range(0,  i):
        P[k] += (u-s)/i
    M = min(product(P),1)
        

    print("Case #{}: {}".format(z, M) )
