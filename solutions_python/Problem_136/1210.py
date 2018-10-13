#!/usr/bin/python
import sys


ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
lines=lines[1:]
case=1

def getBest(c,f,x):
 farmcosts={0:0,}
 sec4farm=0
 c=float(c)
 f=float(f)
 x=float(x)

 for fc in range(0,int(x)+1):
  rate=(f * fc) + 2.0
  sec4farm+=(c/rate)
  farmcosts[fc+1]=sec4farm
  time4goal=(x/rate)

 outcomes={}
 lowest=sys.maxint
 for k in farmcosts.keys():
  rate=(f * k)+ 2.0
  sec4win=farmcosts[k]+(x/rate)
  if sec4win < lowest:
   lowest=sec4win
   nf=k
 return(lowest)

for line in lines:
 if line == '':
  continue
 [c,f,x] = line.split(' ')
 output=getBest(c, f, x)
 output='{0:.7f}'.format(output)
 print("Case #" +str(case)+": "+str(output))
 case+=1

