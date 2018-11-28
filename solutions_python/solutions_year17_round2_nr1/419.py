import sys
read = lambda f=int: map(f, sys.stdin.readline().split())
T, = read()
for case in range(T):
    D, N = read()
    hs = []
    for _ in range(N):
        s, v = read()
        hs.append((s,v))
    a, b = 0, D*max(v for s,v in hs)
    for _ in range(100):
        c = (a+b)/2
        good = True
        for s, v in hs:
            # Test if we hit the horse
            if v < c and s*c < D*(c-v):
                good = False
                break
        if good:
            a = c
        else: b = c

    print('Case #{}: {}'.format(case+1, a))

