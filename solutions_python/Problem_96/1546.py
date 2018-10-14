##dict={}
##for i in range(31):
##    dict[i] = [-1,-1]
##
##
##for i in range(11):
##    for j in range(11):
##        for k in range(11):
##            a = sorted([i,j,k])
##            m = max(a) - min(a)
##            s = sum(a)
##            if m == 2:
##                if dict[s][0] < max(a):
##                    dict[s][0] = max(a)
##            elif m < 2:
##                if dict[s][1] < max(a):
##                    dict[s][1] = max(a)

            
dict = {0: [-1, 0], 1: [-1, 1], 2: [2, 1], 3: [2, 1], 4: [2, 2], 5: [3, 2], 6: [3, 2], 7: [3, 3], 8: [4, 3], 9: [4, 3], 10: [4, 4], 11: [5, 4], 12: [5, 4], 13: [5, 5], 14: [6, 5], 15: [6, 5], 16: [6, 6], 17: [7, 6], 18: [7, 6], 19: [7, 7], 20: [8, 7], 21: [8, 7], 22: [8, 8], 23: [9, 8], 24: [9, 8], 25: [9, 9], 26: [10, 9], 27: [10, 9], 28: [10, 10], 29: [-1, 10], 30: [-1, 10]}
            

import sys

a = open(sys.path[0] + "//B-large.in").readlines()
T=int(a.pop(0))

for i in range(T):
    line = a[i].strip().split(" ")
    N = int(line.pop(0))
    S = int(line.pop(0))
    p = int(line.pop(0))
    _list = [int(x) for x in line]
    rez = 0

    for item in _list:
        s,n = dict[item]
        if n>=p:
            rez+=1
        elif S > 0 and s>=p and s>=0:
            rez+=1
            S-=1
    print "Case #" + str(i+1) + ":", rez

            