t=int(raw_input())
p=[0]*t
for o in xrange(t):
    p[o]=str(raw_input())
    y=p[o].split(" ")
    s=y[0]
    lst=list(s)
    k=y[1]
    i=0
    j=0
    c=0
    for i in xrange(len(lst)-int(k)+1):
        if lst[i]=="-":
            c=c+1
            for j in xrange(int(k)):
                if lst[i+j]=="+":
                    lst[i+j]="-"
                else:
                    lst[i+j]="+"
    if lst==["+"]*len(lst):
        print "Case #"+str(o+1)+": "+str(c)
    else:
        print "Case #"+str(o+1)+": "+"IMPOSSIBLE"
