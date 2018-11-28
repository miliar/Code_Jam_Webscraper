t = int(input())
for tt in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]
    time = -1
    for i in range(n):
        hd, hs = [int(s) for s in input().split(" ")]
        time = max(time, (d - hd) / hs)

    res = d / time
    print("Case #{}: {}".format(tt, res))
