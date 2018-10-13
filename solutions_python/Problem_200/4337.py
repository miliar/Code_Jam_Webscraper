# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:41:50 2017

@author: Bodhiswatta
"""

def isNumberTidy(n):
    l = len(str(n))
    if(l == 1):
        return True
    elif int(''.join(sorted(str(n)))) == n:
        return True
    else:
        return False
        

def lastTidyNumber(n):
    l = len(str(n))
    if(l == 1) or int(''.join(sorted(str(n)))) == n:
        return n
    data = list(str(n))
    ptr = 0
    for i in range(l-1):
        if int(data[i]) < int(data[i + 1]):
            ptr = i+1
        elif int(data[i]) > int(data[i + 1]):
            break
    data[ptr] = str(int(data[ptr]) - 1)
    for i in range(ptr+1, l):
        data[i]='9'
    return int(''.join(data))

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
inpFileName = 'B-large.in'
outFileName = 'B-large.OUT.txt'
f = open(inpFileName, 'r')
data = f.readlines()
f.close()
#t = int(input())  # read a line with a single integer
t = int(data[0])
s = ''
for i in range(1, t + 1):
  #n = int(input())  # read a integers, n in this case
  n = int(data[i])
#  found = False
#  while found == False:
#      found = isNumberTidy(n)
#      n -= 1
#  print("Case #{}: {}".format(i, n+1))
#  s += "Case #{}: {}\n".format(i, n+1)
  out = lastTidyNumber(n)
  print("Case #{}: {}".format(i, out))
  s += "Case #{}: {}\n".format(i, out)
f = open(outFileName, 'w')
f.write(s)
f.close()
  # check out .format's specification for more formatting options