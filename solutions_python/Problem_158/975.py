cases=int(raw_input())
for i in xrange(cases):
    x,r,c=map(int,raw_input().split())
    
    if x==1:
        print 'Case #'+str(i+1)+': GABRIEL'
    elif x==2:
        if (r*c)%2==0:
            print 'Case #'+str(i+1)+': GABRIEL'
        else:
            print 'Case #'+str(i+1)+': RICHARD'
    elif x==3:
        if (r*c)%3==0:
            if r==1:
                print 'Case #'+str(i+1)+': RICHARD'
            elif c==1:
                print 'Case #'+str(i+1)+': RICHARD'
            else:
                print 'Case #'+str(i+1)+': GABRIEL'
        else:
            print 'Case #'+str(i+1)+': RICHARD'
    elif x==4:
        if r==3 and c==4:
            print 'Case #'+str(i+1)+': GABRIEL'
        elif r==4 and c==3:
            print 'Case #'+str(i+1)+': GABRIEL'
        elif r==4 and c==4:
            print 'Case #'+str(i+1)+': GABRIEL'
        else:
            print 'Case #'+str(i+1)+': RICHARD'
