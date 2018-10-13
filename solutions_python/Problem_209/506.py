# -*- coding: UTF-8 -*-

import sys
import math


def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(ps, k):
    rh = {}
    rs = {}
    for i in range(len(ps)):
        p = ps[i]
        rh[i] = p[0] * p[1]
        rs[i] = p[0]

    rhs = sorted(rh.items(), key=lambda x: x[1], reverse=True)
    rss = sorted(rs.items(), key=lambda x: x[1], reverse=True)

    ans = 0.0
    for i in range(len(ps) - k + 1):
        max_r = rss[i][1]
        ans_candi = float(max_r * max_r) + 2.0 * max_r * ps[rss[i][0]][1]
        rest = k-1

        if rest > 0:
            for p in rhs:
                ind = p[0]
                if ps[ind][0] > rss[i]:
                    continue
                if ind == rss[i][0]:
                    continue

                ans_candi += 2.0 * p[1]
                rest -= 1
                if rest == 0:
                    break

        ans = max(ans, ans_candi)

    ans *= math.pi

    return format(ans, ".8f")

#input_file = "sample.in"
#input_file = "A-small-attempt0.in"
input_file = "A-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    n = int(l[0])
    k = int(l[1])
    ps = []
    for i in range(n):
        l = f.readline().rstrip().split()
        ps.append((int(l[0]), int(l[1])))

    ans = solve(ps, k)

    print("Case #" + str(tc+1) + ": " + ans)

