# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def makeTidy(n):
  k = findSmallestViol(n)
  while k != -1:
    dec = 10**(len(str(n))-k)
    if n!= dec:
      n -= n%dec
      n -= 1
    else:
      n -= 1
    k = findSmallestViol(n)
  return n

def findSmallestViol(n):
  n = str(n)
  for i in range(len(n)-1,0,-1):
    if int(n[i]) < int(n[i-1]):
      return i
  return -1
  

def isTidy(n):
  if n < 10:
    return True
  else:
    cur = -1
    for i in str(n):
      if cur > i:
        return False
      cur = i
    return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input().strip())  # read a list of integers, 1 in this case
  m = makeTidy(n)
  if not isTidy(m):
    print("Error")
  print "Case #{}: {}".format(i, m)
  
  # check out .format's specification for more formatting options

