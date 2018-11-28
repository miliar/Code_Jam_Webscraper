import math

n = int(input())

for i in range(1, n + 1):
    cur = 0
    N, K = [int(x) for x in input().split(' ')]

    d = math.pow(2, math.floor(math.log(K, 2)))
    x = int((N - (d - 1)) // d)
    y = int((N - (d - 1)) % d)
    if K - d < y:
        x += 1
    min = (x-1) // 2
    max = min + (x-1) % 2
    print("Case #{}: {} {}".format(i, max, min))
