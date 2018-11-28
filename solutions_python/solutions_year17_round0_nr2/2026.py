import sys

t = int(raw_input())

for i in xrange(1, t+1):
  n = int(raw_input().strip())
  if n < 10:
    res = n
  else:
    while n > 10:
      if n <= 10:
        res = n 
        break
      numstr = str(n)
      #check
      j = 0
      while j < len(numstr)-1:
        if int(numstr[j+1]) < int(numstr[j]):
          mod = 10**(len(numstr) - (j+1)) 
          n -= n%mod
          break
        j += 1

      if j == len(numstr) - 1:
        res = n
        break
      n -= 1    

  print "Case #{}: {}".format(i, res)
