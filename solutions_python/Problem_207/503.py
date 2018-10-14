import numpy as np
f_name='tst_input'
f_name='B-small-attempt2.in'

rows=open(f_name,'r').readlines()
t=int(rows[0])
for tt in range(1,t+1):
    n,r,o,y,g,b,v=map(int,rows[tt].split())
    order=sorted([(r,'R'),(b,'B'),(y,'Y')])
    rr=order[2][0]
    maxx=order[2][1]
    yy=order[1][0]
    midd=order[1][1]
    bb=order[0][0]
    minn=order[0][1]

    if rr>(bb+yy):
        print('Case #%d: IMPOSSIBLE'%tt)
        continue
    remaining=yy+bb-rr
    res=''
   # print(maxx,midd,minn)
   # print(rr,yy,bb)
   # print(r,y,b)
    for i in range(remaining):
        res=res+maxx+midd+minn
    for i in range(yy-remaining):
        res=res+maxx+midd
    for i in range(rr-yy):
        res=res+maxx+minn
    print('Case #%d: '%tt+res)

