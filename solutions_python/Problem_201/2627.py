def brStalls(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('tdlarge.out','w')

    for i in range(tc):
        x,people=list(map(int,f.readline().split()))
        nbathRooms=x+2
        s='1'+('0'*x)+'1'
        l=list(s)
        while people!=0:
            zeroes=max(s.split('1'),key=len)
            maxlen=len(zeroes)
            lindex=s.find(zeroes)
            mid=maxlen//2
            people-=1
            if maxlen%2==0:
                place=lindex+mid-1
                l[place]='1'
                ls=l[0:place][::-1].index('1')
                rs=l[place+1:].index('1')
                s=''.join(l)
            else:
                place=lindex+mid
                l[place]='1'
                ls=l[0:place][::-1].index('1')
                rs=l[place+1:].index('1')
                s=''.join(l)
        
        g.write(('Case #%d: %d %d\n')%(i+1,max(ls,rs),min(ls,rs)))
brStalls('C-small-1-attempt0.in')
