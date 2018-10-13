import math

T = int(input())

for I in range(1, T+1):
    n, k = map(int, input().split())

    i = 2
    l = n
    while i - 1 < k:
        l = (l - 1) / 2
        i *= 2

    i //= 2
    _max = round((l - math.floor(l)) * i)
    _min = i - _max
    if k - i + 1 <= _max:
        l = math.ceil(l)
    else:
        l = math.floor(l)

    left = (l - 1) // 2
    if left < 0:
        left = 0
    right = l // 2
    print('Case #%s: %s %s' % (I, right, left))
