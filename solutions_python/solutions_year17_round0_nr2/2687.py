'''
Created on Apr 8, 2017

@author: piesa
'''
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
from pip._vendor.distlib.compat import raw_input
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = str(raw_input()) # read a list of integers, 2 in this case
    n = list(n)
    n = [int(x) for x in n]
    count = len(n) - 1
    while count > 0:
        if n[count] < n[count-1]:
            if n[count-1] == 0:
                n[count-1] = 9
            else:    
                n[count-1] = n[count-1] - 1
                n[count] = 9
                for j in range(count,len(n)):
                    n[j] = 9   
        count = count - 1
    n = [str(x) for x in n]
    str1 = ''.join(n) 
    if len(str1) > 1:
        str1 = str1.lstrip("0")
    print("Case #{}: {}".format(i, str1))
# check out .format's specification for more formatting options 