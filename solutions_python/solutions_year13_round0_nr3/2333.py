import sys
import math

def isfair(a):
  b = 0
  temp = a
  while temp:
    b = (b*10) + (temp%10)
    temp = int(temp/10)
  if a == b:
    return 1
  return 0

def check():
  res = 0
  t = sys.stdin.readline().split()
  a = int(t[0])
  b = int(t[1])
  sa = int(math.ceil(math.sqrt(a)))
  sb = int(math.floor(math.sqrt(b)))
  for i in range(sa, sb+1):
    if isfair(i) and isfair(i*i):
      res = res + 1
  return res
  

T = int(sys.stdin.readline())
for i in range(T):
  print "Case #%d: %s" % (i+1, check())
