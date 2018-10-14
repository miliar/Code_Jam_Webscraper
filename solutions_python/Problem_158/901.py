n = raw_input()
for i in xrange(1,int(n)+1):
    s = raw_input()
    q,r,c = s.split()
    X=int(q)
    R=int(r)
    C=int(c)
    if X == 1:
        print 'Case #'+str(i)+': GABRIEL'
    elif X == 2:
        if (R == 1 or R == 3) and (C == 1 or C ==3):
            print 'Case #'+str(i)+': RICHARD'
        elif (R == 1 or R == 3)and (C == 2 or C == 4):
            print 'Case #'+str(i)+': GABRIEL'
        elif R == 2 and (C == 1 or C == 2 or C == 3 or C == 4):
            print 'Case #'+str(i)+': GABRIEL'
        elif R == 4:
            print 'Case #'+str(i)+': GABRIEL'
    elif X == 3:
        if R == 1:
            print 'Case #'+str(i)+': RICHARD'
        elif R == 2 and C == 3:
            print 'Case #'+str(i)+': GABRIEL'
        elif R == 2 and (C == 1 or C == 2 or C == 4):
            print 'Case #'+str(i)+': RICHARD'
        elif R == 3 and C ==1:
            print 'Case #'+str(i)+': RICHARD'
        elif R == 3 and (C == 2 or C ==3 or C ==4):
            print 'Case #'+str(i)+': GABRIEL'
        elif R == 4 and C == 3:
            print 'Case #'+str(i)+': GABRIEL'
        elif R == 4 and (C == 1 or C == 2 or C == 4):
            print 'Case #'+str(i)+': RICHARD'
    elif X == 4:
        if R == 1 or R == 2:
            print 'Case #'+str(i)+': RICHARD'
        elif R == 3 and C==4:
            print 'Case #'+str(i)+': GABRIEL'
        elif R == 3 and (C ==1 or C ==2 or C == 3 ):
            print 'Case #'+str(i)+': RICHARD'
        elif R == 4 and (C ==1 or C ==2):
            print 'Case #'+str(i)+': RICHARD'
        elif R == 4 and (C==3 or C == 4):
            print 'Case #'+str(i)+': GABRIEL'


