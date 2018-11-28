import sys


f = open(sys.argv[1])
data = f.readlines()
f.close()

c = int(data.pop(0))

for i in range(c):
    points,D = map(long,data.pop(0).split())

    positions = []
    for j in range(points):
         P,V = map(long,data.pop(0).split())
         for vi in range(V):
             positions.append(P)


    distances = [pi-pj for pi,pj in zip(positions[1:], positions[:-1])]

    t = 0.
    tmax = 0.
    
    for d in distances:
        t = max(0.,(t + D - d)) 
        tmax = max(t,tmax)

    print "Case #"+str(i+1)+":" ,tmax/2.

    del(distances)
