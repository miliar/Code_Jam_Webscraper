import sys
n=int(sys.stdin.readline().strip())
for c in range(1,n+1):
    s=int(sys.stdin.readline().strip())
    for i in range(s): sys.stdin.readline().strip()
    q=int(sys.stdin.readline().strip())
    se=[]
    sw=0
    for i in range(q):
        st=sys.stdin.readline().strip()
        if st not in se:
            if len(se)==s-1:
                sw=sw+1
                se=[st]
            else:
                se.append(st)
    print "Case #"+str(c)+":",sw
