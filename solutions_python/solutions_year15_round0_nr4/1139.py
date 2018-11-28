tt = int(input())
num=tt
while(tt):
    ary = map(int,raw_input().split())
    x = ary[0]
    r = ary[1]
    c = ary[2]
    flag = 1
    rc = r*c
    if (x==1):
        flag = 0
    elif (x==2):
        if (rc%2==0):
            flag = 0
    if(rc%x==0 and flag):
        if r >=x:
            if c>(x/2):
                flag = 0
        elif c>=x:
            if r>(x/2):
                flag = 0
    if(flag):
         print 'Case #%d: RICHARD'%(num-tt+1)
    else:
         print 'Case #%d: GABRIEL'%(num-tt+1)
    tt-=1
