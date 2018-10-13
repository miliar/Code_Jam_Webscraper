def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(b<0):
        b=-b
    if(a<0):
        a=-a
    a,b=max(a,b),min(a,b)
    while(a%b!=0):
        a,b=b,a%b
    return b




fin=open("B-large.in","r")
fout=open("B-large.out","w")
C=int(fin.readline())
for cas in xrange(1,C+1):
    events=map(int,fin.readline().split())
    n=events.pop(0)
    temp=min(events)
    for i in xrange(n):
        events[i]-=temp
    biggcd=events[0]
    for i in xrange(1,n):
        biggcd=gcd(biggcd,events[i])
    x=(temp/biggcd)*biggcd
    if(x<temp):
        x+=biggcd
    fout.write("Case #"+str(cas)+": "+str(x-temp)+"\n")
        
fin.close()
fout.close()
    
    
    
    
    
