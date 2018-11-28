#!/usr/bin/python

def find_best(pile):
   max_size = 0
   iters = 2 ** len(pile) - 1
   for i in xrange(1, iters):
      px0 = 0
      px1 = 0
      ps0 = 0
      ps1 = 0
      j = 0
      bits = bin(i)[2:].zfill(len(pile))
      for bit in bits:
         if bit == '1':
            px1 ^= pile[j]
            ps1 += pile[j]
         else:
            px0 ^= pile[j]
            ps0 += pile[j]
         j += 1
         
      if px1 == px0:
         max_size = max(max_size, ps0, ps1)
   return max_size

test_cases = int(raw_input())
for i in xrange(test_cases):
   list_size = int(raw_input())
   candies = [ int(x) for x in raw_input().split(' ') ]
   size = find_best(candies)
   print "Case #" + str(i + 1) + ":",
   if size > 0:
      print size
   else:
      print "NO"




