t = int(raw_input())  # read a line with a single integer

def isTidy(x):
    while x > 0:
        if x % 10 < x / 10 % 10:
            return False
        x /= 10
    return True

for i in xrange(1, t + 1):
  n = int(raw_input())
  
  while not isTidy(n):
      n -= 1
  
  print "Case #{}: {}".format(i, n)


