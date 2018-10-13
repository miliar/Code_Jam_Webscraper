from math import sqrt

num_cases = int(raw_input())

for case in range(1, num_cases + 1):
    data = raw_input()
    data = data.split(" ")

    R = 2
    C = float(data[0])
    F = float(data[1])
    X = float(data[2])

    k = int(X/C - R/F - 1)

    if k < 0:
        k = 0

    farm_time = 0.0

    ratio = F/R
    cur_ratio = 0
    for i in range(k):
        farm_time = farm_time + 1/(1+cur_ratio)
        cur_ratio = cur_ratio +ratio

    time1 = C*farm_time/R + X/(R+k*F)

    time2 = C*farm_time/R + C/(R+k*F) + X/(R+(k+1)*F)

    output = min(time1, time2)

    print ("Case #" + str(case) + ": " + "%1.7f" % output)