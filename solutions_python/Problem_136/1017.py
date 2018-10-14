#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())
for case in range(T):
  C,F,X=map(float,f.readline().split())
  v=2
  tmin=X/v+1
  td=0
  t=tmin
  while True: 
    tmin=t
    t=td+X/v
    td+=C/v
    v+=F
    if t>tmin:
      break
  print("Case #"+str(case+1)+":",tmin)
     