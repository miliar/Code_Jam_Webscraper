# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(n, us):
    max_u = 0
    for i in us:
        max_u = max(max_u, i)

    if max_u > n - max_u:
        return "IMPOSSIBLE"

    first = -1
    ans = ""
    u_chars = list("ROYGBV")
    prev_max_u = -1
    for i in range(n):
        max_u_ind = -1
        max_u = 0
        for j in range(6):
            if j == prev_max_u:
                continue

            if us[j] == max_u:
                if j == first:
                    max_u_ind = j

            elif us[j] > max_u:
                max_u = us[j]
                max_u_ind = j

        if first < 0:
            first = max_u_ind

        prev_max_u = max_u_ind
        us[max_u_ind] -= 1
        ans += u_chars[max_u_ind]

    if ans[0] == ans[len(ans) - 1]:
        ans = "IMPOSSIBLE"

    return ans

#input_file = "sample.in"
input_file = "B-small-attempt1.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    us = []
    n = int(l[0])
    for i in range(6):
        us.append(int(l[i+1]))
    ans = solve(n, us)
    print("Case #" + str(tc+1) + ": " + ans)

