#! /usr/bin/python2.7
# coding: utf-8

for t in xrange(input()):
    sm,ss = raw_input().split()
    sm = int(sm)
    #ss = zip(range(sm), map(int, ss))
    n = int(ss[0])
    a = 0
    ##print 0,n
    for i in xrange(1,len(ss)):
        ##print i,
        d = int(ss[i])
        if n >= i:
            n += d
            ##print 'C|',n
        elif d == 0:
            ##print 'Z|',n
            pass
        else:
            ##print 'S|',(i-n)+d+n,i-n,a
            a += i - n
            n += (i - n) + d
    ##print n,a

    #print sm,ss
    print 'Case #%d: %d' % (t + 1, a)



