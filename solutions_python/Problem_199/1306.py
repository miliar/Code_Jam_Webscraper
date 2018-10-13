with open('a.out', 'w') as f:
    m = int(input())
    for c in range(m):
        p, n = input().split()
        n = int(n)
        p = [1 if o == '+' else 0 for o in p]
        i = 0
        for k in range(0, len(p) - n + 1):
            if p[k] == 0:
                i += 1
                for j in range(n):
                    p[k + j] ^= 1
        print('Case #{0}:'.format(c + 1), 'IMPOSSIBLE' if 0 in p else i, file=f)
