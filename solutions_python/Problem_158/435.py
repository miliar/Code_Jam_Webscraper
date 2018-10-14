__author__ = 'yuri'

for case in range(1,int(raw_input())+1):
    X,R,C = map(int,raw_input().split())

    Z = X/2 + X%2

    r = 'RICHARD'
    g = 'GABRIEL'

    if (R*C)%X:
        result = r
    elif X<=2:
        result = g
    elif R<Z or C<Z or (R<X and C<X):
        result = r
    elif (R==Z or C==Z) and (R*C/X<=2) and X>3:
        result = r
    else:
        result = g
 #   print 'X:%d, R:%d, C:%d' % (X,R,C)
    print 'Case #%d: %s' % (case,result)
