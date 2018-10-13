#!/usr/bin/python

import sys

def solve():
  def judge(l):
    for i in range(1,len(l)):
      if not l[i]==l[i-1]: return False
    else: return True
  
  g = [f.pop(0) for i in range(4)]
  f.pop(0)
  flag=1
  pr = []
  for i in range(4): pr+= [[g[i][j] for j in range(4)]]
  for i in range(4): pr+= [[g[j][i] for j in range(4)]]
  pr += [[g[i][i] for i in range(4)]]
  pr += [[g[i][3-i] for i in range(4)]]
  for i in pr:
    if '.' in i: 
      flag = 0
      continue
    if judge(i)==True: return str(i[0])+" won"
    if "T" in i:
      i.remove('T')
      if judge(i)==True: return str(i[0])+" won"
  else:
    if flag: return "Draw"
    else: return "Game has not completed"


infile=open("A-large.in",'r')
f=map(lambda s:s.strip(),infile.readlines())
infile.close()
N = int(f.pop(0))
out=open("A-large-result",'w')
for n in range(N):
  out.write("Case #%s: %s\n"%(n+1, solve()))
out.close()