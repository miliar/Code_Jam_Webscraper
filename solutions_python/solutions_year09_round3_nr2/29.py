import math

T = int(raw_input())

for k in xrange(1,T+1):
    N = int(raw_input())
    x = []
    y = []
    z = []
    vx = []
    vy = []
    vz = []
    for t in xrange(0,N):
        arr = [ int(temp) for temp in raw_input().split(' ')]
        x.append(arr[0])
        y.append(arr[1])
        z.append(arr[2])
        vx.append(arr[3])
        vy.append(arr[4])
        vz.append(arr[5])
    
    xmas = 1.0*sum(x)/N
    ymas = 1.0*sum(y)/N
    zmas = 1.0*sum(z)/N
    
    for t in xrange(0,N):
        x[t] += vx[t]        
        y[t] += vy[t]
        z[t] += vz[t]

    vxmas = 1.0*sum(x)/N - xmas
    vymas = 1.0*sum(y)/N - ymas
    vzmas = 1.0*sum(z)/N - zmas
    
    if (vxmas*vxmas+vymas*vymas+vzmas*vzmas != 0):
        tmin = -(vxmas*xmas+vymas*ymas+vzmas*zmas)/(vxmas*vxmas+vymas*vymas+vzmas*vzmas)
    else:
        tmin = 0

    tmin = max(0,tmin)
    xmas = xmas+vxmas*tmin
    ymas = ymas+vymas*tmin
    zmas = zmas+vzmas*tmin
    dmin = math.sqrt(xmas*xmas+ymas*ymas+zmas*zmas)

    print "Case #%d: %.6f %.6f"%(k,dmin,tmin)

