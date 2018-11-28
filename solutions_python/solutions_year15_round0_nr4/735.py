T=int(input())
i=0
while i<T:
    xrc=[int(i) for i in input().split(' ')]
    x,r,c=xrc[0],xrc[1],xrc[2]
    w=min(r,c)
    h=max(r,c)
    sq=w*h
    #print('x',x,' r',r,' c',c)
    if x==1:
        out='GABRIEL'
    if x>r and x>c:
        out='RICHARD'
    elif x<=6:
        if x>1 and w==1 and x!=2:
            out='RICHARD'
        elif x>1:
            if x==4 or x==5 or x==6:
                if w<3:
                    out='RICHARD'
                else:
                    out='GABRIEL'
            else:
                if sq%x==0:
                    out='GABRIEL'
                else:
                    out='RICHARD'
        
         
    print('Case #'+str(i+1)+': '+out)
    i=i+1
