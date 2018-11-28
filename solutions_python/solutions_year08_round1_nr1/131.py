f = open("A-large.in","r")
cases = int(f.readline())
for c in range(1,cases+1):
  size = int(f.readline())
  line = f.readline().split()
  x = [int(s) for s in line]
  x.sort()
  line = f.readline().split()
  y = [int(s) for s in line]
  y.sort(reverse=True)
  sum = 0
  for idx in range(size):
    sum = sum + (x[idx] * y[idx])
  print "Case #%d: %d" %(c,sum)
f.close()