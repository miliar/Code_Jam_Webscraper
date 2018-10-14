test = int(input())
num=test
while(test):
    array = map(int,raw_input().split())
    x = array[0]
    r = array[1]
    c = array[2]
    flag = True
    rc = r*c
    if (x==1):
        print 'Case #%d: GABRIEL'%(num-test+1)
        flag = False
    elif (x==2):
        if (rc%2==0):
            print 'Case #%d: GABRIEL'%(num-test+1)
            flag = False
    if(rc%x==0 and flag):
        if r >=x:
            if c>(x/2):
                print 'Case #%d: GABRIEL'%(num-test+1)

                flag = False
        elif c>=x:
            if r>(x/2):
                print 'Case #%d: GABRIEL'%(num-test+1)
                flag = False
    if(flag):
         print 'Case #%d: RICHARD'%(num-test+1)
    test-=1
