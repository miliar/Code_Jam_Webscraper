import fileinput,math
import numpy as np
outr=open('out.txt','w')
l = [ map(int,line.split()) for line in fileinput.input('A-large.in') ]
i=0
c=1
while(i<l[0][0]):
    d=l[c][0]
    n=l[c][1]
    s=[]
    f=0
    for x in range(c+1,c+n+1):
        if(f<(float(d-l[x][0])/l[x][1])):
            f=(float(d-l[x][0])/l[x][1])
            
    
    outr.write('Case #%d: %.7f\n'%(i+1,d/f))       
    c=x+1
    i=i+1
outr.close()
