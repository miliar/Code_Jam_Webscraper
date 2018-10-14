#!/usr/bin/python
import sys

inp = [l.strip() for l in sys.stdin if l.strip()!='']
T = int(inp[0])
l = 1
for t in range(T):
  secs = 0
  line = inp[l].split(" ")
  pos = [1,1]
  move = [0,0]
  for p in range(int(line[0])):
    c = 0 if line[2*p+1]=='B' else 1
    n = int(line[2*p+2])
    
#    print (p,c,n)
    r=(pos[c]-move[c], pos[c]+move[c])
#    print "robot ",c," has to press ",n," and now is in ",r
    dist = 0
    if n<r[0]:
      # walk left
      dist = r[0]-n
#      print "move left ",dist," to ",n
    elif n>r[1]:
      dist = n-r[1]
#      print "move right ",dist," to ",n
    else:
#      print "can push now"
      pass
    # press
    secs += dist+1
    move[1-c] += dist+1
    move[c] = 0
    pos[c] = n
#    print "robot",(1-c)," is now in ",pos[1-c]," +/- ",move[1-c]
#    print "seconds ",secs
#    print "-----------"


  l += 1
  print "Case #%d: %d" % (t+1, secs)

