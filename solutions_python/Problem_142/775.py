from itertools import *

def med(x):
 pass

def SUB(x):
 O = []
 S = x[0]
 #print x
 now = 1
 for i in x[1:]:
  if i == S[-1]:
   now+=1
  else:
   O.append(now)
   S+=i
   now = 1

 O.append(now)
 return (O,S)
for T in xrange(input()):
 print "Case #%d:"%(T+1),
 S = [ SUB(raw_input()) for i in xrange(input())]
 
 if not all([S[0][1]==S[i][1]  for i in xrange(1,len(S))]):
  print "Fegla Won"
  continue
 S = [ i[0] for i in S ]
 
 #for i in S:  print i
 
 #print 
 S = [ (sorted(list(i))) for i in zip(*S) ]
 B = [ int(round(1.0*sum(i)/len(i))) for i in S ]
 
 ans = 0
 
 for i in xrange(len(S)):
  ans += sum(abs(S[i][j] - B[i]) for j in xrange(len(S[i])))
 print ans
  
  
  
  
  
  