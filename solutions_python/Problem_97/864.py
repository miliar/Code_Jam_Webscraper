#
import re
import math
#f = open("C-large.in","r")
#fo = open("C-large.out","w")
f = open("C-small-attempt0.in","r")
fo = open("C-small.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
i = 0
T = int(lines[i])
for icase in range(T):
      # set parameters
      i = i + 1
      l = re.split(" ",lines[i])
      [A,B] = [int(x) for x in l]
      #print(A,B)
      cA = str(A)
      digit = len(cA)
      npair = 0
      for n in range(A,B+1):
            cn = str(n)
            for d in range(1,digit):
                  cm = cn[d:]+ cn[:d]
                  m = int(cm)
                  if n < m and m <= B:
                        npair = npair +1
                        #print(n,m)
            
      print("Case #",icase+1,": ",npair,sep="",file=fo)
      print("Case #",icase+1,": ",npair,sep="")

#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

