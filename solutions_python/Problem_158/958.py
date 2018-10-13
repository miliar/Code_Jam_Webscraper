__author__ = "TitanUser"

import math
total = int(input())

for i in range(0, total):
    num = [int(i) for i in input().split(' ')]
    x = num[0]
    r = num[1]
    c = num[2]
    q = math.ceil(math.sqrt(x))
    res = ""

    if ((r*c) % x) == 0:
        if (((q >= r or q >= c) and x % 2 == 0) or (q > r or q > c)) and q != x:
            res = "RICHARD"
        else:
            res = "GABRIEL"
    else:
        res = "RICHARD"

    print("Case #{0}: {1}".format((i+1), res))