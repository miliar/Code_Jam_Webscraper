import math
for T in range(input()):
    NC,NJ=map(int,raw_input().split())
    AC=[map(int,raw_input().split()) for n in range(NC)]
    AJ=[map(int,raw_input().split()) for n in range(NJ)]
    if NC==2:
        a,b,c,d=sorted(AC[0]+AC[1])
        if c-b>=720:
            s=2
        elif d-a<=720:
            s=2
        else:
            s=4
    elif NJ==2:
        a,b,c,d=sorted(AJ[0]+AJ[1])
        if c-b>=720:
            s=2
        elif d-a<=720:
            s=2
        else:
            s=4
    elif NC==1:
        s=2
    elif NJ==1:
        s=2
    else:
        a,b,c,d=sorted(AC[0]+AJ[0])
        s=2
    print "Case #{}: {}".format(T+1,s)
