import sys
import os
import math

def maxabovep(N,S,p,t):
  t.sort(reverse=True)
  numabove = 0
  for ti in t:
    if math.floor(float(ti-1)/3)+1 >= p:
      numabove+=1
    else:
      break
  t=t[numabove:]
  for ti in t:
    if S == 0:
      break
    if ti <= 2:
      break
    if math.floor(float(ti-2)/3)+2 >= p:
      numabove+=1
      S-=1
    else:
      break
  return numabove

if __name__ == "__main__":
  f=open(sys.argv[1])
  fw=open(sys.argv[1]+".answer",'w')
  T = f.readline()
  
  linenum=1
  for line in f:
    line = map(int,line.split())
    ans = maxabovep(line[0],line[1],line[2],line[3:])
    fw.write("Case #"+str(linenum)+": "+str(ans)+"\n")
    linenum+=1

  f.close()
  fw.close()
