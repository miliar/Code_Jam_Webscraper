#
import re
import math
def gcd( a, b ):
    while b != 0:
        r = a % b
        a = b
        b = r
    if a < 0:
        return -a
    else:
        return a

#f = open("A-large.in","r")
#fo = open("A-large.out","w")
f = open("B-small-attempt3.in","r")
fo = open("B-small-attempt3.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
nlines = len(lines)
i = 0
se = []
query = []
C = int(lines[i])
for icase in range(C):
      # set parameters
      i = i + 1
      l = re.split(" ",lines[i])
      N = int(l[0])
      t = [int(x) for x in l[1:]]
      t.sort()
      min_t = min(t)
      diff_t = [ t[j+1] - t[j] for j in range(len(t)-1) if t[j+1] - t[j] != 0 ]
      g = diff_t[0]
      for j in range(len(diff_t)-1):
            g = gcd(g,diff_t[j+1])
      y = int((min_t-1)/g+1)*g - min_t
      print("Case #",icase+1,": ",y,sep="",file=fo)
      print("Case #",icase+1,": ",y,sep="")


#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

