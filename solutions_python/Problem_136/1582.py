import sys
T=int(sys.stdin.readline())
buffer=[]
bufferx=[]
buffert=[]
for i in xrange(T):
    P=[float(x) for x in sys.stdin.readline().strip('\n').split()]
    buffer.append(P)
#print buffer
for j in xrange(T):

    C=buffer[j][0]
    F=buffer[j][1]
    X=buffer[j][2]
    #print buffer[j][0]
    time=0
    tf=2
    while X/tf > (X/(F+tf)+C/tf):
        time+=C/tf
        tf=F+tf
    time+=X/tf
    print "Case #"+str(j+1)+": "+str(format(time,'.7f'))



