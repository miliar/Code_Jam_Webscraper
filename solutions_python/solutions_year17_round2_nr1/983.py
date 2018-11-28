#!/usr/bin/python3

import fileinput
from collections import deque
from collections import OrderedDict
from math import log
from math import floor
from math import ceil

f = fileinput.input()
T = int(f.readline())


for case in range(T):

    D, N = map(int, f.readline().strip().split())

    mx  = 0

    for i in range(N):
        K, S = map(int, f.readline().strip().split())
        time = (D - K)/S
        mx = max(mx, time)


    print("Case #" + str(case + 1) + ":", D/mx )

