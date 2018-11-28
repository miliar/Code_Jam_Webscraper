import numpy as np
from time import time

def solve(S):
    nums = []
    flag = 1
    while(len(S)>0 and flag==1):
        flag = 0
        if 'Z' in S:
            S.remove('Z')
            S.remove('E')
            S.remove('R')
            S.remove('O')
            nums.append(0)
            flag = 1
        if 'X' in S:
            S.remove('S')
            S.remove('I')
            S.remove('X')
            flag = 1
            nums.append(6)
        if 'W' in S:
            S.remove('T')
            S.remove('W')
            S.remove('O')
            nums.append(2)
            flag = 1
        if 'G' in S:
            S.remove('E')
            S.remove('I')
            S.remove('G')
            S.remove('H')
            S.remove('T')
            nums.append(8)
            flag = 1


    flag = 1
    while(len(S)>0 and flag==1):
        flag = 0
        if 'H' in S:
            S.remove('T')
            S.remove('H')
            S.remove('R')
            S.remove('E')
            S.remove('E')
            nums.append(3)
            flag = 1
    flag = 1
    while(len(S)>0 and flag==1):
        flag = 0
        if 'R' in S:
            S.remove('F')
            S.remove('O')
            S.remove('U')
            S.remove('R')
            nums.append(4)
            flag = 1

    flag = 1
    while(len(S)>0 and flag==1):
        flag = 0
        if 'F' in S:
            S.remove('F')
            S.remove('I')
            S.remove('V')
            S.remove('E')
            nums.append(5)
            flag = 1

    flag = 1
    while(len(S)>0 and flag==1):
        flag = 0
        if 'V' in S:
            S.remove('S')
            S.remove('E')
            S.remove('V')
            S.remove('E')
            S.remove('N')
            nums.append(7)
            flag = 1

    flag = 1
    while(len(S)>0 and flag==1):
        flag = 0
        if 'I' in S:
            S.remove('N')
            S.remove('I')
            S.remove('E')
            S.remove('N')
            nums.append(9)
            flag = 1
        if 'O' in S:
            S.remove('O')
            S.remove('E')
            S.remove('N')
            nums.append(1)
            flag = 1

    if(len(S)>0):
        print S
        print nums
    nums.sort()
    return nums



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = list(raw_input())
    nums = solve(s)
    num = ''.join([str(k) for k in nums])
    print "Case #{}: {}".format(i, num)
# check out .format's specification for more formatting options
