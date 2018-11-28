import sys
bufferf=[]
buffera=[]
true=[]

T=int(sys.stdin.readline().strip('\n'))
n=0
b=0
value=[None]*T*2
for i in xrange(T):
    for k in xrange(2):
        A=int(sys.stdin.readline().strip('\n'))
        A=(A+4*n)-1
        n=n+1
        buffera.append(A)
        for j in xrange(4):
            F=[int(x) for x in sys.stdin.readline().strip('\n').split()]
            bufferf.append(F)
l=T*2

for m in xrange(0,l-1,2):
    check=0
    
    getkey=None
    for p in xrange(4):
        key=bufferf[buffera[m]][p]

        for y in xrange(4):
            if(key==bufferf[buffera[m+1]][y]):
                check=check+1
                getkey=key
    if(getkey):
        value[b]=getkey
    else:
        value[b]=None    
    b=b+1    

    true.append(check)


for z in xrange(T):
    if(true[z] > 1):
        print "Case #"+str(z+1)+": Bad magician!"
    elif(true[z] == 0):
        print "Case #"+str(z+1)+": Volunteer cheated!"
    else:
        print "Case #"+str(z+1)+": " +str(value[z])


