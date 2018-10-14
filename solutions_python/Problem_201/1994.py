# C.py - Bathroom Stalls
# jreiter

import math

for t in range(int(input())):
  n, k = [int(x) for x in input().split()]
  s = list(range(math.ceil(n/2)+1)) + list(reversed(range(math.floor(n/2)+1)))
  flag = 0.5
  if len(s) % 2 == 0:
    s[int(len(s)/2)-1] += flag

  while k > 1:
    m = max(range(len(s)), key=s.__getitem__)

    s[m] = 0

    # update left
    i = 1
    while s[m-i] > i:
      s[m-i] = i
      i += 1
    if s[m-i] == s[m-i+1] :
      s[m-i] += flag if s[m-1] != 0 else 0      

    # update right
    i = 1
    while s[m+i] > i:
      s[m+i] = i
      i += 1
    if s[m+i-1] == s[m+i]:
      s[m+i-1] += flag if s[m-1] != 0 else 0

    k -= 1
 #   print(s)

 # print("")

  m = max(range(len(s)), key=s.__getitem__)
  y = math.ceil(s[m]-1)
  z = math.floor(s[m]-1)

  print("Case #{}: {} {}".format(t+1, y, z))