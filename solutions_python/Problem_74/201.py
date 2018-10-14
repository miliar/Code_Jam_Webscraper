from sys import stdin

for c in xrange(1, 1+int(stdin.readline().strip())):
  foo = stdin.readline().split()
  N = int(foo[0])
  presses = foo[1:]
  #print presses
  # last acted at:
  lastact = { 'O' : 0, 'B' : 0 }
  lastpos = { 'O' : 1, 'B' : 1 }
  elapsed = 0
  for i in xrange(0, N):
    bot = presses[i*2]
    button = int(presses[i*2+1])
    #print bot + "->" + button
    lastact[bot] = max(lastact[bot]+abs(button-lastpos[bot]), elapsed)+1
    lastpos[bot] = button
    elapsed=lastact[bot]
    #print lastact, lastpos, elapsed
  print "Case #" + str(c) + ": " + str(elapsed)
    
    
    
  
  