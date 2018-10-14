t=int(input())
for ta in range(t):
    c=raw_input()
    c=c.split(" ")
    n=c[0]
    del c[0]
    po=1
    pb=1
    to=0
    tb=0
    t=0
    u=""
    for i in range(len(c)/2):
        #print "po %d, pb %d,to %d, tb %d, tt %d" %(po,pb,to,tb,tt)
        if c[2*i]=='B':
            tt=abs(int(c[2*i+1])-pb)
            if u=="O" and to>tb:
                tt=max(0,tt-to+tb)
                tb=max(tb,to)
            pb=int(c[2*i+1])
            tb=tb+tt+1
            u="B"
        else:
            tt=abs(int(c[2*i+1])-po)
            if u=="B" and tb>to:
                tt=max(0,tt-tb+to)
                to=max(tb,to)
            po=int(c[2*i+1])
            to=to+tt+1
            u="O"
    print "Case #%d: %d"%(ta+1,max(tb,to))
