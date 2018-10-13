import sys

if len(sys.argv)<2:
  exit()
  

  
      

fname = sys.argv[1]
f = open(fname, "r")

T = int(f.readline())



for i in range(T):
  A,B,K = [int(x) for x in f.readline().split()]
  r = 0
  for a in range(A):
    for b in range(B):
      if a&b < K:
        r += 1
  print "Case #%d: %d" % (i+1, r)
  
f.close()