def solve(d, h):
    h = sorted(h, reverse=True, key=lambda x: x[0])
    ct = None
    for di, sp in h:
        t = (d - di) / float(sp)
        #print("ct: {}, t:{}".format(ct, t))
        if ct is not None:
            if t > ct:
                ct = t
        else:
            ct = t
        #print(di, sp, ct)
    return d / float(ct)


n = int(input())
for i in range(1, n+1):
    d, k = tuple(map(int, input().split()))
    h = []
    for j in range(k):
        pos, speed = tuple(map(int, input().split()))
        h.append((pos, speed))
    print("Case #{}: {}".format(i, solve(d, h)))