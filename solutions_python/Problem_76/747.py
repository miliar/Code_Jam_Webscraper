#!/usr/bin/python

def list_xor(l, start, end):
   ret = 0
   for i in range(start, end):
      ret ^= l[i]
   return ret

def list_sum(l, start, end):
   ret = 0
   for i in range(start, end):
      ret += l[i]
   return ret

import sys

fp = open(sys.argv[1], 'r')

num_cases = int(fp.readline())

for i in range(0, num_cases):
   fp.readline()
   line = fp.readline()
   words = line.split()

   nums = []

   for w in words:
      nums.append(int(w))

   nums.sort()

   ans = -1

   for j in range(1, len(nums)):
      if list_xor(nums, 0, j) == list_xor(nums, j, len(nums)):
         ans = list_sum(nums, j, len(nums))
         break

   if ans == -1:
      print "Case #" + str(i+1) + ": NO"
   else:
      print "Case #" + str(i+1) + ": " + str(ans)
