# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys


def tidy(num, n):
    if is_tidy(num, n):
        return num
    
    ret = []
    
    if num[0] > n:
        ret.append(num[0])
        return ret + tidy(num[1:], num[0])
    else:
        if len(num)>1:
            ret.append(n)
            new_num = declement(num[1:])
            if len(new_num) == 1 and new_num[0] == 0:
                return ret
            else:
                return ret + tidy(new_num, n)
        else:
            return ret.append(num[0])
        
def is_tidy(num, n):
    if n < num[0]:
        return False
    
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            return False
    return True
    
def declement(num):
    u"""逆順の配列"""
    ret = []
    if num[0] == 0:
        ret.append(9)
        new_num = declement(num[1:])
        if len(new_num) == 1 and new_num[0] == 0:
            return ret
        else:
            return ret + new_num
    else:
        num[0] -= 1
        return num 
    
with open(sys.argv[1], "r") as f:
    count = int(f.readline())
    
    out = []
    for i in range(count):
        S= f.readline().rstrip('\r\n')
        S_num = []

        for num_str in list(S):
            S_num.append(int(num_str))
        S_num.reverse()
        
        tidy_num = tidy(S_num, 9)
        tidy_num.reverse()
        
        tidy_str = ""
        for num in tidy_num:
            tidy_str += str(num)
        
        out.append("Case #%d: %s\n"%(i+1, tidy_str))

with open(sys.argv[1] + "_out.txt", "w") as f:
    f.writelines(out)

