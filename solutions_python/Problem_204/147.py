# https://code.google.com/codejam/contest/5304486/dashboard#s=p1
from collections import defaultdict
from math import ceil

if __name__ == "__main__":
    filein = open('20171AB.in', 'r')
    fileout = open('20171AB.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        print(t)
        fileout.write('Case #%d: ' % (t + 1))
        [N, P] = map(int, filein.readline().split())
        Q = list(map(int, filein.readline().split()))
        l = [[] for _ in range(N)]
        for i in range(N):
            weights = list(map(int, filein.readline().split()))
            for j in range(P):
                servings_lb = max(1, int(ceil(weights[j] / 1.1 / Q[i])))
                servings_ub = int(weights[j] / 0.9 / Q[i])
                if servings_ub >= 1 and servings_ub * Q[i] * 1.1 >= weights[j]:
                    l[i].append([servings_lb, servings_ub])

            l[i].sort(key=lambda x: x[1])
            l[i].sort(key=lambda x: x[0])
        ans = 0
        while all(x for x in l):
            [s, e] = l[0][0]
            # Check possibility
            tuples = [(x[0], n) for n, x in enumerate(l)]
            max_s = max(tuples)[0][0]
            min_e = min(tuples)[0][1]
            if max_s <= min_e:
                ans += 1
                for i in range(len(l)):
                    del l[i][0]
            else:
                for n in (x[1] for x in tuples if x[0][0] <= min_e):
                    del l[n][0]
        fileout.write(str(ans) + '\n')

    filein.close()
    fileout.close()
