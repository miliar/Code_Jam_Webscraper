import sys
rl = lambda: sys.stdin.readline()

def solve(c):
  p = 2.0
  C,F,X = map(float, rl().strip().split())
  r = X/p
  i=1
  psum = 0
  while True:
    r1 = X/(p+F*i)
    psum += C/(p+(i-1)*F)
    r1 += psum
    if r1<r:
      r= r1
    else:
      break
    i+=1

  print "Case #%d: %.7f" % (c+1, r)
 
n = int(rl())
for i in range(n):
  solve(i)

