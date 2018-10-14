__author__ = 'deniskrut'

# https://code.google.com/codejam/contest/2974486/dashboard#s=p0

import sys

t_num = int(sys.stdin.readline())
mat_size = 4

for i in range(0, t_num):
    a1 = int(sys.stdin.readline())
    m1 = []
    for j in range(0, mat_size):
        m1.append([int (x) for x in sys.stdin.readline().split()])

    a2 = int(sys.stdin.readline())
    m2 = []
    for j in range(0, mat_size):
        m2.append([int (x) for x in sys.stdin.readline().split()])

    match_num = 0
    num_res = -1
    for r1 in range(0, mat_size):
        for r2 in range(0, mat_size):
            if m1[a1 - 1][r1] == m2[a2 - 1][r2]:
                match_num += 1
                num_res = m1[a1 - 1][r1]

    res = "Bad magician!"
    if match_num == 1:
        res = num_res
    if match_num == 0:
        res = "Volunteer cheated!"

    print "Case #" + str(i + 1) + ": " + str(res)