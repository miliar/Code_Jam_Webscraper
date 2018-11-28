import math

with open('b.out', 'w') as fl:
    t = int(input())
    for case in range(t):
        n, p = map(int, input().split())
        recipe = tuple(map(int, input().split()))
        #packages = tuple(sorted(map(int, input().split())) for _ in range(n))
        counts = {}
        packages = [{} for _ in range(n)]
        for ing in range(n):
            for amount in map(int, input().split()):
                c1 = math.floor(amount / (0.9 * recipe[ing]))
                c2 = math.ceil(amount / (1.1 * recipe[ing]))
                while c2 <= c1:
                    f = counts.get(c2, [0] * n)
                    f[ing] += 1
                    counts[c2] = f
                    c2 += 1

        N = 0
        #print(counts)
        for key, val in counts.items():
            N += min(val)

        print('Case #{0}:'.format(case + 1), min(N, p), file=fl)

