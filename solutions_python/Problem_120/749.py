import math
 
n = int(raw_input())
for i in range(0,n):
    a = []
    b = raw_input()
    a = b.split()
    r = int(a[0])
    t = int(a[1])
    p = (2*r)-1
    p = p*p
    p = p+8*t
    p = math.sqrt(p)
    p = p-(2*r)+1
    p = p/4
    p = int(p)
    h = (2*p)+(2*r)-1
    h = h*p
    while(h>t):
        p = p-1
        h = (2*p)+(2*r)-1
        h = h*p
    print('Case #%d: %d'%(i+1,p))