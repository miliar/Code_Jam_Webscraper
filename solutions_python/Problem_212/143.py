# https://code.google.com/codejam/contest/5314486/dashboard
from collections import Counter

if __name__ == "__main__":
    filein = open('20172A.in', 'r')
    fileout = open('20172A.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        [N, P] = map(int, filein.readline().split())
        KS = []
        G = list(map(int, filein.readline().split()))
        G_remainder = [g % P for g in G]
        G_r_count = dict(Counter(G_remainder))
        ans, current = G_r_count.get(0, 0), 0
        G_r_count[0] = 0
        strategies = [
            [{1: 2}],
            [{1: 1, 2: 1}, {1: 3}, {2: 3}],
            [{2: 2}, {1: 1, 3: 1}, {2: 1, 1: 2}, {3: 2, 2: 1}, {1: 4}, {3: 4}]
        ]
        strategy = strategies[P - 2]
        for s in strategy:
            multiplier = min(G_r_count.get(num, 0) // s[num] for num in s)
            ans += multiplier
            if multiplier != 0:
                for num in s:
                    G_r_count[num] -= multiplier * s[num]
        if any(G_r_count[num] != 0 for num in G_r_count):
            ans += 1
        fileout.write(str(ans) + '\n')

    filein.close()
    fileout.close()
