#
import re
import math
f = open("A-large.in","r")
fo = open("A-large.out","w")
#f = open("A-small-practice.in","r")
#fo = open("A-small-practice.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
nlines = len(lines)
i = 0
se = []
query = []
N = int(lines[i])
for icase in range(N):
      # set parameters
      i = i + 1
      [n,k] = re.split(" ",lines[i])
      [N,K] = [int(n),int(k)]
      base = 2**N
      X = K - int(K/base)*base
      if X == base - 1:
            ans = 'ON'
      else:
            ans = 'OFF'
      print("Case #",icase+1,": ",ans,sep="",file=fo)
      #print("Case #",icase+1,": ",ans,sep="")


#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

