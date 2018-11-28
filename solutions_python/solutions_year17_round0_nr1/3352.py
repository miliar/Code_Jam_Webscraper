def panCakes(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('panCakesSmall.out','w')
    for i in range(tc):
        string,v=f.readline().split()
        length=len(string)
        s=list(string)
        templ=s[:]
        templr=s[::-1]
        k=int(v)
        minuscount=s.count('-')
        if minuscount==1:
            g.write(('Case #%d: IMPOSSIBLE\n')%(i+1))
        elif minuscount==0:
            g.write(('Case #%d: 0\n')%(i+1))
        else:
            happy=False
            cnt=0
            while not happy:
                right=s.index('-')
                temp=right+k
                if temp<=length:
                    cnt+=1
                    for idx in range(right,temp):
                        if s[idx]=='-':
                            s[idx]='+'
                        else:
                            s[idx]='-'
                    minuscount=s.count('-')
                    if minuscount==0:
                        happy=True
                    elif minuscount==1 or templ==s or templr==s:
                        break

                elif temp>k:
                    cnt+=1
                    left=length - 1 - s[::-1].index('-')
                    temp=right-k+1
                    for idx in range(temp,left+1):
                        if s[idx]=='-':
                            s[idx]='+'
                        else:
                            s[idx]='-'
                    minuscount=s.count('-')
                    if minuscount==0:
                        happy=True
                    elif minuscount==1 or templ==s or templr==s:
                        break                                        

            if happy:
                g.write(('Case #%d: %d\n')%(i+1,cnt))
            else:
                g.write(('Case #%d: IMPOSSIBLE\n')%(i+1))
    f.close()
    g.close()
panCakes('A-large.in')

