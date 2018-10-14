#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     13/04/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
result = []
with open('1B-A-small-attempt1.IN') as f:
    T = int(f.readline())

    for i in range(0, T):
        arr = f.readline().strip().split(' ')
        A = int(arr[0])
        N = int(arr[1])
        ms = [int(x) for x in f.readline().strip().split(' ')]
        ms.sort()
        if A == 1:
            rs = N
        else:
            cost = []
            for j in range(0, N):
                if A < ms[j]:
                    err = math.ceil( math.log( (ms[j] )/(A-1.0), 2) )
                    if err < N-j:
                        cost.append(err)
                        A = pow(2, err) * (A -1) + 1 + ms[j]
                    else:
                        break;
                elif A == ms[j]:
                    A = 2*A - 1 + ms[j]
                    cost.append(1)
                else:
                    cost.append(0)
                    A = A + ms[j]
            rs = 0
            l = len(cost)
            print cost
            for j in range(0, l):
                if cost[j] < l-j:
                    rs += cost[j]
                else:
                    rs += l - j
                    break
            rs += N - l
        result.append(int(rs))
    ########################33

print result
with open('1B-A-small-attempt1.OUT', 'w') as f:
    for  i in range(0, T):
        f.write("Case #%d: %s\n" % (i+1, result[i]) )
