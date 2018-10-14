#!/usr/bin/env python
out = open("luces",'w')
casos = int(raw_input())
j=1
while(j <= casos):
    n,k = (int(a) for a in raw_input().split(" "))
    aux = int((2**n)-1)
    if k %  (aux+1) == aux:
        out.write("Case #%s: ON\n"%j)
    else:
        out.write("Case #%s: OFF\n"%j)
    j+=1
out.close()
        

