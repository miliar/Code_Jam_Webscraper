import sys

for i in range(int(sys.stdin.readline())):
    c, f, x = map(float, sys.stdin.readline().split())
    t, n = x / 2, 0
    while True:
        n += 1
        t_ = sum(c / (2 + k * f) for k in range(n)) + x / (2 + n * f)
        if t_ > t:
            break
        t = t_
    print('Case #{}: {:.7f}'.format(i + 1, round(t, 7)))
