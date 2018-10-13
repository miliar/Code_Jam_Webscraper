
import math


g = open('output.txt', 'w')

f = open('A-large (1).in', 'r')

t= int(f.readline())
for i in range(t):
    s=f.readline().split()
    d=int(s[0])
    n=int(s[1])
    s=f.readline().split()
    k =int(s[0])
    sp= int(s[1])
    maxtime=(d-k)/sp

    
    for j in range(n-1):
        s=f.readline().split()
        k =int(s[0])
        sp= int(s[1])
        time=(d-k)/sp
        if time>maxtime:
            maxtime=time
    
    res=d/maxtime
    g.write("Case #" +str(i+1) +": "+str(res) + "\n")
g.close()
        

