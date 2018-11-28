t = int(input())
for i in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]
    lis = []
    for j in range(1, n + 1):
        k, s = [float(s) for s in input().split(" ")]
        time = (d - k) / s
        lis.append(time)
    print("Case #{}: {}".format(i, d/max(lis)))


