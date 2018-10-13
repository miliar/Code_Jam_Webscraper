import math
fw = open('z6.txt', 'w')
fr = open('B-small-attempt3.in', 'r')
t=int(fr.readline())
for k in range(1,t+1):
    n=int(fr.readline())
    s=[]
    s=fr.readline().split()
    for i in range(n):
        s[i]=int(s[i])
    s1=s.copy()
    r=max(s)
    
    j=r
    for i in range(1,200):
   
        a=j/2
        b=math.floor(a)
        c=math.ceil(a)
        s.remove(j)
      
        s.append(b)
        s.append(c)
        
        j=max(s)
        if j+i<=r:
            r=j+i


          
    r1=max(s1)
    j=r1
    
    for i in range(1,200):
        
        if j!=9:
         a=j/2
         b=math.floor(a)
         c=math.ceil(a)
         s1.remove(j)
         s1.append(b)
         s1.append(c)
        else:
            s1.remove(9)
            s1.append(3)
            s1.append(6)
        j=max(s1)
        if j+i<=r1:
            r1=j+i
                    
    
                   
        
    fw.write('Case #'+str(k)+': ' +str(min(r,r1))+'\n')    
   
fr.close()
fw.close()
