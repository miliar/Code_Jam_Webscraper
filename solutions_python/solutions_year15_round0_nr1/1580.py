t= int(input())
n=t
while(t):
    ar = raw_input().split()
    max_shy = int(ar[0])
    shy = ar[1]
    count = 0
    friends = 0
    cc=0
    count+=int(shy[0])
    for i in range(1,max_shy+1):
        if shy[i] == '0':
            continue
        cc = i - count
        if cc>0:
            count+=cc
            friends+=cc
            count+=int(shy[i])
        else:
            count+=int(shy[i])
    print 'Case #%d:'%(n-t+1),friends
    t-=1
