#! /usr/bin/python

T = int(raw_input())
for test in range(T):
    print 'Case #%d:' % (test+1),
    X, R, C = [int(x) for x in raw_input().split()]
    if C >= X:
        if R >= X-1:
            if C%X == 0 or R%X == 0:
                print 'GABRIEL'
            else:
                print 'RICHARD'
        else:
            print 'RICHARD'
    elif R >= X:
        if C >= X-1:
            if C%X == 0 or R%X == 0:
                print 'GABRIEL'
            else:
                print 'RICHARD'
        else:
            print 'RICHARD'
    else:
        print 'RICHARD'
                
            
            
