from __future__ import division

def time(D,indata):
 K = float(indata[0])
 S = float(indata[1])
 t = (D-K)/S
 return t

fname = "A-large"

with open(fname + ".in","r") as f:
 inp = [l.strip('\n') for l in f.readlines()]

f = open(fname + ".out","w")
j=1
for i in range(int(inp[0])):
 case = inp[j].split(' ')
 D = int(case[0])
 N = int(case[1])
 T = 0
 for k in range(N):
  t = time(D,inp[j+1+k].split(' '))
  if T<t:
   T = t
 V = float(D) / T
 f.write("Case #" + str(i+1) + ": " + str(V) + "\n")
 j = j+1+N

f.close()




