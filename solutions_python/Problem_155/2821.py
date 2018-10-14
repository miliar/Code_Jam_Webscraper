import sys
rl = sys.stdin.readline

for T in range(int(rl())):
    X = list(map(int, rl().split()[1]))
    t = 0
    f = 0
    for i,x in enumerate(X):
        if t < i:
            y = i - t
            t += y
            f += y
        t += x
    print('Case #{}: {}'.format(T+1, f))
