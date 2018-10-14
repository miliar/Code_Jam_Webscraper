t = int(input())

for i in range(t):
    d, n = [int(x) for x in input().strip().split(' ')]
    slowest_time = 0
    for j in range(n):
        k, s = [float(x) for x in input().strip().split(' ')]
        if (float(d)-k)/s > slowest_time:
            slowest_time = (d-k)/s

    time = d / slowest_time

    print("Case #{}: {:.6f}".format(i+1,time))
