import sys, re

L,D,N = sys.stdin.readline().split()
w = ""
for i in range(0,int(D)):
  w += str(sys.stdin.readline())

for i in range(0,int(N)):
  pat = str(sys.stdin.readline())
  pat = pat.replace('(','[')
  pat = pat.replace(')',']')  
  print "Case #"+str(i+1)+": "+str(len(re.findall(pat, w)))


