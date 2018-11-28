#!/usr/bin/python
import math

f = open('test.in')
f2 = open('res.out', 'wb')
a = f.readline()
a = f.readline()
i =1;
string = "Case #$: "
while a:
    out = ""
    p = a.split()
    lo = int(p[0])
    hi = int(p[1])
    out = str(string.replace("$", str(i)))
    
    lolo = int(math.floor(math.sqrt(lo)))
    hihi = int (math.floor(math.sqrt(hi)))

    while lolo * lolo < lo:
        lolo += 1
    res = 0
    k = lolo
    while (k*k) <= hi:
        strk = str(k)
# print k
        if strk == strk[::-1]:
            sqres = k * k;
            sqstr = str(sqres)
            if sqstr == sqstr[::-1]:
                res +=1
#               print sqstr
        k+=1
    
    i+=1
    out = out + str(res)+"\n"
    f2.write(out)
    a = f.readline()
