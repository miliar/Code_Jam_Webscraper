import math
f=open('C-small-attempt0.in','r')
r=open('out.out','w')
t=int(f.readline().strip('\n'))
for k in range(t):
    [a,b]=[int(i) for i in f.readline().strip('\n').split()]
    y=0
    #print a,b
    for i in range(a,b+1):
        s=str(i)
        if s==s[::-1]:
            #print i
            p=math.sqrt(i)
            #print p
            if p==int(p):
                p=int(p)
                s=str(p)
                if s==s[::-1]:
                    y+=1
    r.write("Case #"+str(k+1)+": "+str(y))
    print "Case #"+str(k+1)+": "+str(y)
    r.write('\n')
r.close()
