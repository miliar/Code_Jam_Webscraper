import sys

def getcenter(d):
    data = zip(*d)
    return list(map(lambda x:sum(x)/len(x), data))

def time(x,y,z,vx,vy,vz):
    if vx**2 + vy**2 +vz**2 == 0:
        return 0.0
    else:
        #return -(x+y+z)/(vx+vy+vz)
        return -(x*vx + y*vy + z*vz)/(vx**2 + vy**2 +vz**2)

def getdis(center,t):
    x,y,z,vx,vy,vz = center
    xc = x + vx * t
    yc = y + vy * t
    zc = z + vz * t
    return pow((xc**2 + yc**2 + zc**2), 0.5)

def func(f):
    N = int(f.readline())
    fireflies = []
    for i in range(N):
        t = [int(i) for i in f.readline().split()]
        fireflies.append(t)
    center = getcenter(fireflies)
    #print(fireflies, center)
    t = time(*center)
    if t < 0:
        t = 0
    d = getdis(center, t)
    return d,t

f = open(sys.argv[1])
T = int(f.readline())
for i in range(1, T+1):
    d,t = func(f)
    print("Case #%d: %.8f %.8f" % (i, d, t))
