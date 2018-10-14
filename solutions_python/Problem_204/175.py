import sys
import math
from collections import defaultdict

T = int(raw_input())

for tc in xrange(1, T + 1):
    N, P = map(int, raw_input().split())
    recipe = map(int, raw_input().split())

    packages = []

    for i in xrange(N):
        packages.append(sorted(map(int, raw_input().split())))

    curr = [ 0 ] * N

    minR = 1;
    ans = 0

    while True:
        all_good = True
        #print minR, curr, ans
        for i in xrange(N):
            low  = math.ceil(minR * recipe[i] * 0.9)
            high = math.floor(minR * recipe[i] * 1.1)

            found = False
            for j in xrange(curr[i], P):
                if packages[i][j] < low:
                    curr[i] = j + 1
                elif packages[i][j] <= high:
                    found = True
                    break;
                else:
                    break

            if not found:
                all_good = False
                break

        if not all_good:
            minR += 1
            if max(curr) == P:
                break;
            continue
        ans += 1

        curr = [c + 1 for c in curr]


    print "Case #%d: %d" % (tc, ans)