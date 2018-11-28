#!/usr/bin/env python


f1 = file('b-in.txt')

t = int(f1.readline())

for kk in range(1, t+1):
    s = (f1.readline()).split()
    c = float(s[0])
    f = float(s[1])
    x = float(s[2])
#    print c,f,x
    max = x/2.0
    n = 1
    while 1:
#        print 'n='+str(n)
        ret = c/2.0
#        print ret
        for i in range(1,n):
#            print c/(2.0+f*i)
            ret = ret + c/(2.0+f*i)
#        print ret, max
        if ret > max:
            break
        ret = ret + x/(2+n*f)
#        print x/(2+n*f),ret, max
        if ret < max:
            max = ret
        elif ret > max:
            break
        n = n + 1
    print 'Case #'+str(kk)+': '+str(max)