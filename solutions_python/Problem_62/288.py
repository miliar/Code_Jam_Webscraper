f=open('input','r')
fo=open('out','w')
z=-2
count=0
ls=[]
c=0
for line in f:
    if z==-2:
        testno=int(line)
    elif z==-1:
        n=int(line)
        z=0
    else:
        if n>=0:
            l=line.split()
            t=int(l[0]) , int(l[1])
            for x in ls:
                if x[0] < t[0]:
                    if x[1]> t[1]:
                        count=count+1
                else:
                    if x[1]< t[1]:
                        count=count+1
            ls.append(t)
            n=n-1
            if n==0:
                c=c+1
                fo.write( "Case #" + str(c) + ": " + str(count) +'\n')
                ls=[]
                count=0
                z=-1
    if z==-2:
        testno=int(line)
        z=-1