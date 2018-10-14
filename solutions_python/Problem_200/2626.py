def f(l):
    p = 0
    v = l[0]
    for i, x in enumerate(l):
        if x > v:
            p, v = i, x
        elif x < v:
            return p

T = int(raw_input())
for i in range(T):
    N = [int(c) for c in raw_input()]
    x = f(N)
    if x is not None:
        N[x] -= 1 
        for j in range(x+1, len(N)):
            N[j] = 9
    print('Case #{}: {}'.format(i+1, int(''.join(str(d) for d in N), 10)))
