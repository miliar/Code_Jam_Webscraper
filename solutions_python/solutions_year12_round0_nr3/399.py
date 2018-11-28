#-*-coding:utf-8-*-

# 1-10   : 0
# 11-100 : 12->21 13->31 .. 19->91 (8)
#          23->32 24->42 .. 29->92 (7)
#         => 8 + 7 + 6 + .. + 1 = 9 * 4 = 36
# 101-1000 : 

"""
Input 
 	
Output 
 
4
1 9
10 40
100 500
1111 2222
Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287

"""

import os, sys, math

def count_recycle_pair(figures, minimum, maximum):
    x = minimum
    count = 0
    mul = 10 ** (figures - 1)
    while x <= maximum:
        r = x
        for i in range(figures):
            r = (r // 10) + (r % 10) * mul
            if r > x and minimum <= r <= maximum:
                count += 1
            elif r == x:
                break
            pass
        x += 1
        pass
    return count

fh = open(sys.argv[1])
for t in range(int(fh.readline())):
    A, B = fh.readline().split(' ')
    count = 0
    numbers = [int(x) for x in A]
    print('Case #{0}: {1}'.format(t+1, count_recycle_pair(len(A), int(A), int(B))))
    pass
