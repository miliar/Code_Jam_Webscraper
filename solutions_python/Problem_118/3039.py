import math
v=[]
t=input ()
x=0;

for x in range (1,t+1) :
            s=0
            a,b=raw_input().split()
            for i in range (long(a), long(b)+1) : 
             i=str(i)
             if i==i[::-1] :
                           if str(math.sqrt(long(i))).replace(".0","") == str(math.sqrt(long(i))).replace(".0","")[::-1] : s=s+1
                                                                                                             
            v.append(s)
for i in range (0,t) :
                      print 'Case #%s:' % (i+1) ,v[i]          
                
