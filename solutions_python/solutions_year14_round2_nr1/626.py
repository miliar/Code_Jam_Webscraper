import sys
import math

if len(sys.argv)<2:
  exit()
  

  
def solve(d, n):
  pattern = ""
  ll = []
  for s in d:
    t = 1
    l = []
    pp = s[0]

    for c in s[1:]:
      if c!=pp[-1]:
        pp += c
        l.append(t)
        t = 1
      else:
        t+=1

    l.append(t)
    if pattern == "":
      pattern = pp
    elif pp != pattern:
      return False, 0 
    
    ll.append(l)
#    print l
  
  avgl = [0]*len(pattern)
  for x in ll:
    for i in range(len(pattern)):
      avgl[i]+=x[i]
  
#  print avgl
  for i in range(len(pattern)):
    avgl[i] = round(avgl[i]*1./n)
#  print avgl
  r = 0
  for x in ll:
    for i in range(len(pattern)):
      r += math.fabs(x[i]-avgl[i])
      
  return True, r

fname = sys.argv[1]
f = open(fname, "r")

T = int(f.readline())



for i in range(T):
  n = int(f.readline())
  d = []
  for j in range(n):
    d.append(f.readline().strip())
  
  ist, res = solve(d, n)
  
  if ist:
    print "Case #%d: %d" % (i+1, res) 
  else:
    print "Case #%d: Fegla Won" % (i+1) 
    
    
  
f.close()
