import pprint


TEST = "C-small-1-attempt0"
f1 = open(TEST+".in")
f2 = open(TEST+".out", "w")

T_max = int(f1.readline())
for T in range(T_max):
    f2.write("Case #%s: " % (T+1))
    print("Case #%s " % (T+1))

    N,K = map(int, f1.readline().split())
    U = float(f1.readline())
    P = list(map(float, f1.readline().split()))
    print(P)

    if(1. * N - sum(P) <= U):
        f2.write("%.8f\n" % 1.)
        continue

    l = 0.
    r = 1.
    while(r - l > 1e-10):
        m = (l+r)/2.
        out = 0
        for i in range(N):
            if(P[i] < m):
                out += m - P[i]

        if(out < U):
            l = m
        elif(out > U):
            r = m
        else:
            break
    m = (r + l) / 2.
    print(m)

    ans = 1.
    for i in range(N):
        if(P[i] > m):
            ans *= P[i]
        else:
            ans *= m

    f2.write("%.8f\n" % ans)
