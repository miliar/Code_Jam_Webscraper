
t = int(input())

for c in range(t):
    d, n = [int(item) for item in input().split()]
    slowest = 0;
    for i in range(n):
        k, s = [int(item) for item in input().split()]
        l = d-k
        time = l/s
        slowest = max(time, slowest)
    print("Case #%d: %f" % (c+1, d/slowest))
