'''
Created on Apr 11, 2014

@author: shaqal
'''

T = int(raw_input())

for i in range(0,T):
    c,f,x = raw_input().split()
    c= float(c)
    f= float(f)
    x= float(x)
    t1 = x/2.0
    t2 = 0.0
    n=0
    
    while True:
        n+=1
        S = 0.0
        for j in range(1,n+1):
            S += (j/(2+(n-j)*f))
        
        t2 = (x+ n*c +f*c*S)/(2+n*f)
    
        if t2<t1:
            t1 = t2
            t2 = 0
        else:
            print "Case #"+str(i+1)+": "+str(t1)
            break
    
    
    
    
    
    
    