t = int(input())
n=t
while(t):
    ar = map(int,raw_input().split())
    x = ar[0]
    r = ar[1]
    c = ar[2]
    flag = True
    rc = r*c
    if (x==1):
        print 'Case #%d: GABRIEL'%(n-t+1)
        flag = False
    elif (x==2):
        if (rc%2==0):
            print 'Case #%d: GABRIEL'%(n-t+1)
            flag = False
    if(rc%x==0 and flag):
        if r >=x:
            if c>(x/2):
                print 'Case #%d: GABRIEL'%(n-t+1)

                flag = False
        elif c>=x:
            if r>(x/2):
                print 'Case #%d: GABRIEL'%(n-t+1)
                flag = False
    if(flag):
         print 'Case #%d: RICHARD'%(n-t+1)
    t-=1
