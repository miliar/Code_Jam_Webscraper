from math import log
from math import ceil


f=open("/home/anurag/Downloads/B-large.in",'r')
o=open("out.txt",'w')

T=int(f.readline())

for p in range(T):
    
    x = f.readline().split()
    L,P,C = long(x[0]),long(x[1]),long(x[2])
    if P <= C*L:
        ans = 0
    else :
        a = C*L
        b = ceil(P/float(C))
        
        if b<=a:
            count = 1
        else:
            count = 2
            while C*a < b:
                a = C*a
                b = ceil(b/float(C))
                count += 2
        
            if b<=a:
                count -= 1
                
        ans = long(log(count,2) + 1)
    o.write("Case #%d: %d\n" %(p+1,ans))
        
