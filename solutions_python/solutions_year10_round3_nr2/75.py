import math

for case in range(1, int(input()) + 1):
    (L, P, C) = map(int, input().split())
    i = 0
    while L * C < P:
        L *= C
        i += 1
    p = 0
    while i > 0:
        i = math.ceil((i - 1) / 2)
        p += 1
    print('Case #%d: %d' % (case, p))
