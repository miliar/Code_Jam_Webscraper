def doCase(ln):
  chunks = ln.split()
  chunks = chunks[1:] #ignore previous buttons
  loc = {'O':1, 'B':1}
  last_move = None
  total = 0
  this_bot = 0
  
  for step in xrange(0,len(chunks),2):
    name = chunks[step]
    button = int(chunks[step+1])
    #print name, button
    
    num_move = abs(button - loc[name])
    
    if last_move != name:
      num_move = max(0,num_move - this_bot)            
      this_bot = 0
      last_move = name
    
    loc[name] = button
    total += num_move + 1
    this_bot += num_move + 1
  return total
  

import sys

stdin = sys.stdin

num = sys.stdin.readline()

#print num

for i in xrange(int(num)):
  ln = stdin.readline()
  
  val = doCase(ln)
  print 'Case #%s: %s' % (i+1, val )