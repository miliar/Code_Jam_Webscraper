def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)

def tidy(n):
  v = [int(i) for i in str(n)]
  for i in xrange(len(v)-1):
    if v[i] > v[i+1]:
      return False
  return True

def call(v):
  v = str(v)
  if tidy(int(v)):
    return int(v)
  brkpos = len(v)
  for i in range(1, len(v)):
    if v[i-1] > v[i]:
      brkpos = i
      break
  prefix = int(v[:brkpos]) - 1
  #print prefix, len(v)-brkpos
  return call(int(str(prefix) + "9"*(len(v)-brkpos)))
    
    
    
        
  
def call2(n):
  last = 1
  v = int(raw_input())
  for i in xrange(v,0,-1):
    if tidy(i):
      printout(n+1, i)
      return
  print "aaa"
"""
for i in range(1,1000):
  call(i)
  call2(i)
exit()
"""
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call(raw_input()))