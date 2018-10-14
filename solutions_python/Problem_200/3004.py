#!/usr/bin/python

import sys

def tidy_num():
   n = int(input())
   lst = str(n)
   if len(lst) == 1 or sorted(lst) == list(lst):
       return n
   x = -1
   for i in range(len(lst)-1):
       if lst[i] > lst[i+1]:
           x = len(lst) - i - 1
           break
   while i >= 1:
       if lst[i-1] == lst[i]:
           x += 1
       else:
           break
       i -= 1
   return n if x < 0 else n//10**x * 10**x - 1

for case in range(int(input())):
    print ('Case #%d: %s' % (case+1, tidy_num()))
