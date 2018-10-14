__author__ = 'deniskrut'

import sys

def checkLane(lane, n, m):
    validation_lane = []
    for i_n in range(0, n):
        local_validation = []
        for i_m in range(0, m):
            local_validation.append(False)
        validation_lane.append(local_validation)
    #validation_lane = [[False] * m] * n
    for i_m in range(0, m):
        max_col = 1
        for i_n in range(0, n):
            if lane[i_n][i_m] > max_col:
                max_col = lane[i_n][i_m]
        for i_n in range(0, n):
            if lane[i_n][i_m] == max_col:
                validation_lane[i_n][i_m] = True
    for i_n in range(0, n):
        max_row = 1
        for i_m in range(0, m):
            if lane[i_n][i_m] > max_row:
                max_row = lane[i_n][i_m]
        for i_m in range(0, m):
            if lane[i_n][i_m] == max_row:
                validation_lane[i_n][i_m] = True
    valid = True
    for i in range(0, m):
        for j in range(0, n):
            if not valid:
                break
            valid = valid and validation_lane[j][i]
    return valid

t = int(sys.stdin.readline())

res = []

for i in range(0, t):
    nm = sys.stdin.readline().split()
    n = int(nm[0])
    m = int(nm[1])

    lane = []
    for j in range(0, n):
        lane.append(sys.stdin.readline().split())

    local_res = checkLane(lane, n, m)
    res.append(local_res)

for i in range(0, t):
    res_str = "NO"
    if res[i]:
        res_str = "YES"
    print "Case #" + str(i + 1) + ": " + res_str