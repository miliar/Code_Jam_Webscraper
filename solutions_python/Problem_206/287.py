# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(d, hs):
    last_time = 0.0
    for house in hs:
        last_time = max(last_time, float(d - house[0]) / float(house[1]))

    ans = float(d) / last_time

    return str(ans)

#input_file = "sample.in"
#input_file = "A-small-attempt0.in"
input_file = "A-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    d = long(l[0])
    n = int(l[1])

    hs = []
    for i in range(n):
        l = f.readline().rstrip().split()
        hs.append((long(l[0]), long(l[1])))

    ans = solve(d, hs)
    print("Case #" + str(tc+1) + ": " + ans)

