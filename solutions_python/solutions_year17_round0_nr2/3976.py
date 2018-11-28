def printOut(I, p):
  print "Case #{}: {}".format(I, p)

def lastTidyNumber(n):
  ns = str(n)
  i = 0
  while (i < len(ns)-1) and (ns[i+1] >= ns[i]):
    i += 1

  if i==len(ns)-1: # n is clean
    return n

  elif ns[i] > ns[i+1]:
    n = int(ns[0:i] + str(int(ns[i])-1) + "9"*len(ns[i+1:]))
    return lastTidyNumber(n)

t = int(raw_input())  # read a line with a single integer
for I in xrange(1, t + 1):
  n = int(raw_input());

  printOut(I, lastTidyNumber(n))


