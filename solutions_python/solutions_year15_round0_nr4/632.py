T = int(raw_input())
for i in range(T):
    X, R, C = [int(j) for j in raw_input().split()]
    
    if X==1:
        r='GABRIEL'
    elif X==2:
        if (R*C)%2:
            r='RICHARD'
        else:
            r='GABRIEL'
    elif X==3:
        if R*C in [6, 9, 12]:
            r='GABRIEL'
        else:
            r='RICHARD'
    else:
        if R*C in [12, 16]:
            r='GABRIEL'
        else:
            r='RICHARD'

    print"Case #"+str(i+1)+": "+str(r)
