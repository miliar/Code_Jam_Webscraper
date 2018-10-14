#!/usr/bin/python
from collections import deque
import sys

f = open(sys.argv[1],'r')
n = int(f.readline())
for a in range(1,n+1):
  line1=f.readline().split(" ")
  line2=f.readline().split(" ")
  R=int(line1[0])
  k=int(line1[1])
  queue=deque(map(lambda x: int(x),line2))
  E=0
  for ride in range(R):
    i=0
    p=0
    while (p+queue[0]<=k) and (i<len(queue)):
      p=p+queue[0]
      E=E+queue[0]
      queue.append(queue.popleft())
      i=i+1
  print "Case #%d: %s"%(a,E)
