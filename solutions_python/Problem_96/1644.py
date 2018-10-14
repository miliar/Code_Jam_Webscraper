import sys

gc=0
for line in open(sys.argv[1]).read().strip().split("\n")[1:]:
    gc+=1
    d = map(int, line.split())
    s = d[1]; p = d[2]; g=d[3:]; c=0    
    limit = 3*p-4
    for x in g:
        if x>=limit:
            z=x%3
            if z == 1 and x-limit>=2: c+=1
            elif z == 0:
                if x/3>=p: c+=1
                elif x != 0 and x/3+1==p and s>0:
                    c+=1; s-=1
            else:
                q=(x-2)/3+1
                if q>=p: c+=1
                elif q+1==p and s>0:
                    c+=1; s-=1
    print "Case #"+str(gc)+": "+str(c)


