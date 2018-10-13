import math

def solve(N, P, recipe, packages):
    def valid(required, real):
        return real <= required * 1.1 and real >= required * 0.9

    S = []
    for i in range(N):
        amt = recipe[i]
        packs = sorted(packages[i])
        s = []
        for pack in packs:
            s_max = int(math.floor((pack / 0.9) / amt))
            s_min = int(math.ceil((pack / 1.1) / amt))

            if s_min <= s_max:
                s.append((s_min, s_max))

        S.append(list(reversed(s)))

    count = 0

    while all(len(s) > 0 for s in S):
        s_min = max(s[-1][0] for s in S)
        s_max = min(s[-1][1] for s in S)

        if s_min <= s_max:
            count += 1
            for s in S:
                s.pop()
            continue

        for s in S:
            if s[-1][1] < s_min:
                s.pop()

    return count

import sys
sys.stdin = open('B-large.in', 'rt')
sys.stdout = open('B-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    N, P = map(int, raw_input().strip().split(' '))

    recipe = map(int, raw_input().strip().split(' '))
    packages = []
    for _ in range(N):
        packages.append(map(int, raw_input().strip().split(' ')))

    print "Case #%d: %s" % (t, solve(N, P, recipe, packages))
