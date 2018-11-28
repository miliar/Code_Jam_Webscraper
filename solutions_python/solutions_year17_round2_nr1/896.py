for _ in range(int(input())):
    D,N = map(int,input().split())
    H = []
    for __ in range(N):
        k,s = map(int,input().split())
        H.append((k,s))

    t = [(D-k)/s for k,s in H]
    print("Case #{}: ".format(_+1),end='')
    print("%.6f" % (D/max(t)))



