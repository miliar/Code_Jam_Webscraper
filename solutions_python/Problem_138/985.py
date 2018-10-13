#!/usr/bin/python3
import fileinput
from collections import deque
from copy import deepcopy
f=fileinput.input()
T=int(f.readline())
for case in range(T):
  N=int(f.readline())
  naoblks=deque(sorted([float(i) for i in f.readline().split()],reverse=True))
  naoblksfk=deepcopy(naoblks)
  kenblks=deque(sorted([float(i) for i in f.readline().split()],reverse=True))
  kenblksfk=deepcopy(kenblks)
  naoscore=0
  kenscore=0
  for m in range(N):
    if naoblks[0]>kenblks[0]:
      naoscore+=1
      kenblks.pop()
      naoblks.popleft()
    elif naoblks[0]<kenblks[0]:
      kenscore+=1
      kenblks.popleft()
      naoblks.popleft()
  naoscorefk=0
  kenscorefk=0
  for n in range(N):
      if naoblksfk[-1]>kenblksfk[-1]:
        naoscorefk+=1
        kenblksfk.pop()
        naoblksfk.pop()
      else:  
        kenscorefk+=1
        kenblksfk.popleft() 
        naoblksfk.pop()
      
  print("Case #"+str(case+1)+":",naoscorefk,naoscore)
     