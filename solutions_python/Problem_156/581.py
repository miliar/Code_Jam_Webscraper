#!/usr/bin/env python 

T = input ()
for cas in xrange (T):
    n = input ()
    a = map (int, raw_input ().split ())
    ans = 9999999999999999
    for x in range (1, max (a)+1):
        t = 0
        for val in a:
            if val > x:
                t += (val-x)/x + ((val-x)%x > 0) 
        ans = min (t + x, ans)
    print 'Case #%i: %i'%(cas+1, ans)

