import sys
import numpy as np

data = sys.stdin.readlines()
t = int(data[0])
for i in range(t):
    print "Case #%d:" % (i+1),

    d = data[i+1].split()

    N = int(d[0])
    R = int(d[1])
    Y = int(d[3])
    B = int(d[5])

    N_arr = np.array([R, Y, B])
    i_sort = np.argsort(N_arr)[::-1]

    N_arr = N_arr[i_sort]
    c_arr = np.array(['r', 'y', 'b'])[i_sort]

    a = N_arr[1] + N_arr[2] - N_arr[0]
    b = N_arr[0] - N_arr[2]
    c = N_arr[0] - N_arr[1]

    if a < 0 or b < 0 or c < 0:
        print "IMPOSSIBLE"
        continue

    ret = ""
    for j in range(a):
        ret += "%c%c%c" % (c_arr[0], c_arr[1], c_arr[2])

    for j in range(b):
        ret += "%c%c" % (c_arr[0], c_arr[1])

    for j in range(c):
        ret += "%c%c" % (c_arr[0], c_arr[2])

    print ret
