import sys, math, random

def permute(s, c):
  global k
  global minscore

  new = ''
  
  times = len(s) / k
  for i in range(times):
    for j in c:
      new += s[i*k+j]

  # calc score
  score = 0
  prev = '!'
  for i in new:
    if i != prev:
      score += 1
    prev = i

  minscore = min(score, minscore)
  

def combo(c, left, s):
  if len(left) == 0:
    permute(s,c)
   
  else:
    for i in range(len(left)):
      
      ccopy = c[:]
      leftcopy = left[:]

      ccopy.append(leftcopy.pop(i))
      combo(ccopy, leftcopy, s)
      
    

inputcases = int(sys.stdin.readline())
for caseno in range(inputcases):
  print 'Case #%d:' % (caseno+1),

  k = int(sys.stdin.readline())
  s = sys.stdin.readline()

  minscore = len(s)
  combo([], range(k), s)

  print minscore
  
  #map(int, sys.stdin.readline().split())
