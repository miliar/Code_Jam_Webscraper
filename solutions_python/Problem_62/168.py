#!/usr/bin/python
import sys

f = open(sys.argv[1],'r')
n = int(f.readline())
for tc in range(1,n+1):
  line=f.readline().rstrip('\n').split(" ")
  N=int(line[0])
  M=[]
  B=[]
  for i in range(N):
    rope=map(lambda x:int(x),f.readline().rstrip('\n').split(" "))
    M.append(rope[1]-rope[0])
    B.append(rope[0])
#  print M
#  print B
  Result=0
  for i in range(N-1):
    for j in range(i+1,N):
      #      print i,j
      if M[i]-M[j]!=0:
        if (float(B[j]-B[i])/(M[i]-M[j]))>0:
          Result=Result+1
  print "Case #%d: %s"%(tc,Result)
