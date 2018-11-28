#!/usr/local/bin/python3

file = open('input.txt', 'r')
n=file.readline()
cps=2.0
case=[]
for i in range(int(n)):
    l=file.readline().rstrip('\n').split(' ')
    c=float(l[0])
    f=float(l[1])
    x=float(l[2])
    if x<=c:
      r=x/cps
    else:
      t=0
      ttc=c/cps
      ttx=x/cps 
      ccps=cps+f
      while (ttx-ttc)>(x/ccps):              
        t=t+ttc
        ttc=c/ccps
        ttx=x/ccps
        ccps=ccps+f
      r=t+ttx  
    case.append(r)  
       
for i in range(len(case)):
    print("Case #{0}: {1:.7f}".format(i+1,case[i]))