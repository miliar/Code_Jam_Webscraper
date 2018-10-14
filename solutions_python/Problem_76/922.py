#
import re
import math
f = open("C-large.in","r")
fo = open("C-large.out","w")
#f = open("A-small-practice.in","r")
#fo = open("A-small-practice.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
nlines = len(lines)
i = 0
se = []
query = []
T = int(lines[i])
for icase in range(T):
      # set parameters
      i = i + 1
      N = int(lines[i])
      i = i + 1
      l = re.split(" ",lines[i])
      c = [int(x) for x in l]
      #cc = [ bin(x) for x in c]
      s = 0
      for x in c:
            s = s ^ x
      if s != 0:
            ans = 'NO'
      else:
            ans = 'YES'
            c.sort()
            mc = sum(c[1:])            
      if ans == 'NO':
            print("Case #",icase+1,": ",ans,sep="",file=fo)
            print("Case #",icase+1,": ",ans,sep="")
      else:
            print("Case #",icase+1,": ",mc,sep="",file=fo)
            print("Case #",icase+1,": ",mc,sep="")

#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

