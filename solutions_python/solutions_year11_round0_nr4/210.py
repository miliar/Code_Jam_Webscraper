from sys import stdin
  
for t in xrange(1, 1+int(stdin.readline().strip())):
  N = int(stdin.readline())
  a = [int(z)-1 for z in stdin.readline().split()]

  
  count=N
  for z in xrange(0,N):
    if a[z] == z:
      count-=1
  print "Case #" + str(t) + ": " + str(count) + ".000000"
