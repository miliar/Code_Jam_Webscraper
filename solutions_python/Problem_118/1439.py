# fairandballarge.py
import sys, math

def is_square(posint):
  if posint == 1: return True
  x = posint // 2
  seen = set([x])
  while x * x != posint:
    x = (x + (posint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True
  
def is_fair(posint):
  s = str(int(posint))
  for i,c in enumerate(s[:len(s)/2]):
    if str(c) != s[len(s)-i-1]: return False
  return True
  
def isqrt(x):
  if x < 0:
    raise ValueError('square root not defined for negative numbers')
  n = int(x)
  if n == 0:
    return 0
  a, b = divmod(n.bit_length(), 2)
  x = 2**(a+b)
  while True:
    y = (x + n//x)//2
    if y >= x:
      return x
    x = y

if __name__ == '__main__':
  T = int(sys.stdin.readline().strip())
  for t in range(T):
    line = sys.stdin.readline().strip()
    A = int(line.split()[0])
    B = int(line.split()[1])
    a = A
    count=0
    for i in range(A,B+1):
      if is_fair(i) and is_square(int(i)) and is_fair(isqrt(i)):
        count+=1
    print "Case #%d: %d" % (t+1,count)
