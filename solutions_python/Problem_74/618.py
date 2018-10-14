# -*- coding: utf-8 -*-
import sys
def find_next(todo, robo, start):
  for r, n in todo[start:]:
    if r==robo:
      return n
  return -1
f = open(sys.argv[1],"r")
T = int(f.readline())
for t in range(T):
  time = 0
  pos_o, pos_b = 1,1
  l = f.readline().split()
  N = int(l[0])
  assert len(l)%2 == 1
  todo = [[l[2*i+1],int(l[2*i+2])] for i in range((len(l)-1)/2)]
  for i in range(len(todo)):
    next_b = find_next(todo, "B", i)
    next_o = find_next(todo, "O", i)
#    print "%d, %d: blue from %d to %d, orange from %d to %d, wait for "%(time,
#	i, pos_b, next_b, pos_o, next_o),
    if todo[i][0]=="B":
#      print "blue",
      steps = abs(pos_b-next_b)+1
      if pos_o > next_o:
	pos_o = pos_o - min(steps, pos_o-next_o)
      if pos_o < next_o:
	pos_o = pos_o + min(steps, next_o-pos_o)
      pos_b = next_b
    else:
      steps = abs(pos_o-next_o)+1
      if pos_b > next_b:
	pos_b = pos_b - min(steps, pos_b-next_b)
      if pos_b < next_b:
	pos_b = pos_b + min(steps, next_b-pos_b)
      pos_o = next_o
#      print "orange",
#    print "this needs %d steps"%steps
    time = time + steps
  
  print "Case #%d: %d"%(t+1, time)

