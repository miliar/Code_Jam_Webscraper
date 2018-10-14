#!/usr/bin/env python
from fractions import gcd
out = open('apocalipsis','w')

casos = int(raw_input())

j=1
while j <= casos:
    aux = [int(a) for a in raw_input().split(" ")]
    n = aux.pop(0)
    aux.sort()
    if n == 2:
        x = aux[1] - aux[0]
        res = aux[1]%x
        if(res != 0):res=x-res
        out.write("Case #%s: %s\n"%(j,res))
    else:
        c,b,a = aux
        x = gcd(a-c,gcd(a-b,b-c))
        res = a%x
        if(res!=0):res=x-res
        out.write("Case #%s: %s\n"%(j,res))
    j+=1
out.close()