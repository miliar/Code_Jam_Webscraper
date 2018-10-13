import math

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    x = math.floor((n - k) / (2 ** math.floor(math.log(k, 2))))
    minimum = maximum = 0
    if x % 2 == 0:
        minimum = maximum = (x / 2)
    else:
        minimum = math.floor(x / 2)
        maximum = math.ceil(x / 2)
    print("Case #%d: %d %d" % (i, maximum, minimum))
