#!/usr/bin/env python
import sys
import bisect

palisquares = []

def palindrome(x):
  if(str(x) == str(x)[::-1]): return True
  else: return False

for i in range(10**7+47):
  if palindrome(i):
    sq = i**2
    if palindrome(sq): palisquares.append(sq)

#print(".)")
#for x in palisquares: print(x)

data = sys.stdin.readlines()
T = int(data[0])

index = 1
for line in data[1:]:
  a, b = line.split()
  a, b = int(a), int(b)
  res = bisect.bisect(palisquares, b)-bisect.bisect_left(palisquares, a)
  print("Case #" + str(index) + ": " + str(res))
  index += 1
