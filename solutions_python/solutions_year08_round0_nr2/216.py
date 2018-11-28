file = open('in')

#lines = file.readlines()

ind = 0
N = int(file.readline())

def getTable(n,t):
    dep = []
    red = []
    for i in xrange(1,n+1):
        li = file.readline()
        li = li.replace(':',' ').split()
        d = int(li[0])*60 + int(li[1])
        r = int(li[2])*60 + int(li[3]) + t
        dep.append(d) 
        red.append(r)
        dep.sort()
        red.sort()
    return (dep,red)

def getNum(dep,red):
    n = 0
    for d in dep:
        if len(red)>0:
            if red[0]>d:
                n+=1
            else:
                red.pop(0)
        else:
            n+=1
    return n

for i in xrange(1,N+1):
    t = int(file.readline())
    
    ind+=1
    li = file.readline().split()

    na = int(li[0])
    nb = int(li[1])
    
    dA,rB = getTable(na,t)
    dB,rA = getTable(nb,t)
    
    
    print 'Case #'+str(i)+':',getNum(dA,rA),getNum(dB,rB) 

    
    
    