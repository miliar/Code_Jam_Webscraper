filename='A-large.in'

f=open(filename)
numCase=int(f.readline())
for i in range(numCase):
    L=f.readline().split()
    dist=int(L[0])
    numH=int(L[1])
    inf=[]
    maxTime=0
    for j in range (numH):
        J=f.readline().split()
        start=int(J[0])
        speed=int(J[1])
        inf.append([start,speed])
        time=1.0*(dist-start)/speed
        if time>maxTime:
            maxTime=time
    mySpeed=1.0*dist/maxTime
    print 'Case '+'#'+str(i+1)+': '+str(mySpeed)

    

