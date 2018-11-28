# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(n, q, hs, ds):

    min_time = [-1.0 for i in range(n)]
    min_time[0] = 0
    for i in range(n-1):
        distance = 0
        for j in range(i+1, n):
            distance += ds[j - 1]
            if distance > hs[i][0]:
                break

            time = min_time[i] + float(distance) / float(hs[i][1])
            if min_time[j] < 0:
                min_time[j] = time
            else:
                min_time[j] = min(min_time[j], time)

    return str(min_time[n-1])

#input_file = "sample.in"
input_file = "C-small-attempt1.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    n = int(l[0])
    q = int(l[1])
    hs = []
    for i in range(n):
        l = f.readline().rstrip().split()
        hs.append((long(l[0]), long(l[1])))

    ds = []
    for i in range(n-1):
        l = f.readline().rstrip().split()
        ds.append(long(l[i+1]))

    l = f.readline().rstrip().split()
    l = f.readline().rstrip().split()

    ans = solve(n, q, hs, ds)
    print("Case #" + str(tc+1) + ": " + ans)

