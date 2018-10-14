t = int(raw_input())
for z in range(1, t + 1):
    d, n = [int(s) for s in raw_input().split(" ")]
    d1 = []
    s1 = []
    for i in range(n):
        d2, s2 = [int(j) for j in raw_input().split(" ")]
        d1.append(d2)
        s1.append(s2)
    p1 = 0
    k2 = 0
    for k1 in range(len(s1)):
        if((float(d) - float(d1[k1])) / s1[k1] > p1):
            p1 = (float(d) - float(d1[k1])) / s1[k1]
            k2 = k1
    d3 = float(d1[k2])
    s3 = float(s1[k2])
    p = float(d) - d1[k2]
    h = p / s1[k2]
    ans = float(d) / h
    print "Case #{}: {}".format(z, "%.6f" %ans)
