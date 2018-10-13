#
import re
import math
         
f = open("B-large.in","r")
#f = open("B-small-practice.in","r")
#f = open("A-large-practice.in","r")

fo = open("B_large.out","w")
#fo = open("B_large.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
T = int(lines.pop(0))
for icase in range(T):
      # set parameters
      line = lines.pop(0)
      cN = line
      order = len(line)
      N = int(line)
      Ns = [ int(i) for i in cN ]
      minN = min(Ns)
      maxN = max(Ns)
      if order == 1:
            ans = N
      else:
            eq = 0
            for j in range(order-1):
                  if Ns[j] > Ns[j+1]:
                        eq = j
                        for k in range(j):
                              if Ns[j] == Ns[k]:
                                    eq = k
                                    break
                        Ns[eq] = Ns[eq] - 1
                        for x in range(eq+1,order):
                              Ns[x] = 9
                        #print(j,Ns[j],Ns[j-1])
                        #Ns[k] = min(Ns[k],Ns[j+1])
            ans = "".join([str(x) for x in Ns])
            ans = ans.lstrip("0")
            
      print("Case #",icase+1,": ", ans, sep="")
      print("Case #",icase+1,": ", ans ,sep="",file=fo)
          
#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

