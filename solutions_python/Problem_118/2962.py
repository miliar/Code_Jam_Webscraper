def ispal(s):
  j=len(s)-1
  for i in range(len(s)/2):
    if s[i]!=s[j]:
      return False
    j-=1
  return True

import gmpy
import math
for i in range(int(raw_input())):
  a, b = [int(j) for j in raw_input().split()]
  c=0
  for j in range(a, b+1):
    if gmpy.is_square(j) and ispal(str(int(math.sqrt(j)))) and ispal(str(j)):
      c+=1
  print "Case #%d: %d" % (i+1, c)