# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:09:58 2017

@author: ntrenchi
"""
def zero_from(num_str, start):
    l = len(num_str)
    num_of_zeros = l - start
    return num_str[:start] + "0" * num_of_zeros
#       
#def tidy_up(num):
#    n = str(num)
#    l = len(n)
#    if l == 1:
#        return num
#    else:
#        i = 0
#        while i < l - 1:
#            if int(n[i]) < int(n[i + 1]):
#                i += 1
#            else:
#                n = zero_from(n, i + 1)
#                n = str(int(n) - 1)
#                break
#        return n

#def test():
#    print(tidy_up(23145))
#    print(tidy_up(21315))
#    print(tidy_up(111111111111111111111110))
    
def tidy_up(num):
    n = str(num)
    l = len(n)
    if l == 1:
        return num
    else:
        i = 0
        while i < l - 1:
            if int(n[i]) <= int(n[i + 1]):
                i += 1
            else:
                n = zero_from(n, i + 1)
                n = str(int(n) - 1)
                return tidy_up(n)
        return n

t = int(input())  # number of test cases
for i in range(1, t + 1):
    last_num_counted = int(input()) # read a list of integers, 2 in this case
    last_tidy_num_counted = tidy_up(last_num_counted)
    print("Case #{}: {}".format(i, last_tidy_num_counted))
