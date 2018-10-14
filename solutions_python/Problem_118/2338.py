#!C:\Python27\python

import math

cases_num = int(raw_input())
for case in range(1, cases_num + 1):
    count = 0;
    start, end = map(int, raw_input().split(" "))
    for num in range(start, end + 1):
        sqrt = math.sqrt(num)
        if sqrt != int(sqrt):
            continue

        sqrt = int(sqrt)
        if str(num) == str(num)[::-1] and str(sqrt) == str(sqrt)[::-1]:
            count = count + 1
        elif len(str(num)) == 1:
            count = count + 1

    print "Case #" + str(case) + ": " + str(count)
