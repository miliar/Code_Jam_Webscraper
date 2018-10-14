t = int(raw_input())  # read a line with a single integer

import numpy as np

for i in xrange(1, t + 1):
    string_N, string_M = [s for s in raw_input().split(" ")]
    N = int(string_N)
    M = int(string_M)
    cake = []
    for n in range(0, N):
        cake.append(raw_input())
        cake_list = [list(word) for word in cake]
    #do right hand pass
    for n in range(0, N):
        for m in range(1, M):
            if cake_list[n][m] == '?':
                cake_list[n][m] = cake_list[n][m-1]
        #do left hand pass
        for m in reversed(range(0,M-1)):
            if cake_list[n][m] == '?':
                cake_list[n][m] = cake_list[n][m+1]

    #then, if there are still ?s, it means that there were only ?s in the whole row
    # so it is safe to copy from the entry above.
    #sweep from top to bottom
    for n in range(1,N):
        for m in range(0,M):
            if cake_list[n][m] == '?':
                cake_list[n][m] = cake_list[n-1][m]

    #then sweep from bottom to top
    for n in reversed(range(0,N-1)):
        for m in range(0,M):
            if cake_list[n][m] == '?':
                cake_list[n][m] = cake_list[n+1][m]

    string_cakes = [''.join(x) for x in cake_list]

    print "Case #{}:".format(i)
    for n in range(0,N):
        print string_cakes[n]
  # check out .format's