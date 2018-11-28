
# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(ps, k):
    #debug(str(ps))
    #debug(str(k))

    ans = 0
    for ind in range(len(ps)):
        if not ps[ind]:
            if ind > len(ps) - k:
                return "IMPOSSIBLE"

            for flip_ind in range(ind, ind + k, 1):
                ps[flip_ind] = not ps[flip_ind]

            ans += 1

    return str(ans)

input_file = "A-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"), 'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    s = l[0]
    ps = []
    for c in s:
        ps.append(c == '+')

    ans = solve(ps, int(l[1]))
    print("Case #" + str(tc+1) + ": " + ans)

