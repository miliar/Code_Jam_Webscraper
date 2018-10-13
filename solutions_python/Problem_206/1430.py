


for i in range(input()):
    d, n = map(int,raw_input().split())
    ks = []

    for j in range(n):
        a, b = map(int, raw_input().split())
        ks.append((d-a)/(b*1.0))
    ans = "{:.6f}".format(d*1.0/max(ks))
    print "Case #{}: {}".format(i+1, ans)


