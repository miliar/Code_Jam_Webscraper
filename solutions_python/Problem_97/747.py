import sys
import os
import math

def numrecycled(A,B):
  num=0
  for n in range(A,B):
    ns = str(n)
    m_found = []
    for i in range(1,len(ns)):
      ns = ns[-1]+ns[:-1]
      m = int(ns)
      if n<m and m<=B and m not in m_found:
        m_found.append(m)
        num+=1
  return num

if __name__ == "__main__":
  f=open(sys.argv[1])
  fw=open(sys.argv[1]+".answer",'w')
  T = f.readline()
  
  linenum=1
  for line in f:
    line = map(int,line.split())
    ans = numrecycled(line[0],line[1])
    fw.write("Case #"+str(linenum)+": "+str(ans)+"\n")
    linenum+=1

  f.close()
  fw.close()
