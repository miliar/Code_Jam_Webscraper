#!/usr/bin/python

ERROR = 0.00000001

def getDistance(x, y, z):
    return (x**2 + y**2 + z**2)**0.5

def calcula(t1, t2, d1, d2, xc, yc, zc, vxc, vyc, vzc):
    dres, tres = -1.0, -1.0
    if (abs(t1 - t2) < ERROR) and (abs(d1 - d2) < ERROR):
        dres, tres = (d1 + d2) / 2, (t1 + t2) / 2
#        dres, tres = d1, t1
    else:
        t0 = (t2 + t1) / 2
        dmedio = getDistance(xc + vxc*t0, yc + vyc*t0, zc + vzc*t0)
        if (dmedio < d1) and (dmedio < d2):
            if (d1 < d2):
                dres, tres = calcula(t1, t0, d1, dmedio, xc, yc, zc, vxc, vyc, vzc)
            else:
                dres, tres = calcula(t0, t2, dmedio, d2, xc, yc, zc, vxc, vyc, vzc)
        else:
            if (d1 < d2):
                if (dmedio < d2):
                    dres, tres = calcula(t1, t0, d1, dmedio, xc, yc, zc, vxc, vyc, vzc)
                else:
                    dres, tres = dmedio, t0
#                    print 'Problemon, d1 y d2 son menores que dmedio'
#                    print 'd1 = %s, d2 = %s, dm = %s, t1 = %s, t2 = %s, tm = %s' % (d1, d2, dmedio, t1, t2, t0)
            else:
                if (dmedio < d1):
                    dres, tres = calcula(t0, t2, dmedio, d2, xc, yc, zc, vxc, vyc, vzc)
                else:
                    dres, tres = dmedio, t0
#                    print 'Problemon, d1 y d2 son menores que dmedio'
#                    print 'd1 = %s, d2 = %s, dm = %s, t1 = %s, t2 = %s, tm = %s' % (d1, d2, dmedio, t1, t2, t0)
    return dres, tres

for case in range(input()):
    N = input()
    xc, yc, zc, vxc, vyc, vzc = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(N):
        x, y, z, vx, vy, vz = map(int, raw_input().split())
        xc += x
        yc += y
        zc += z
        vxc += vx
        vyc += vy
        vzc += vz
#    xc = xc
#    yc = yc
#    zc = zc
#    vxc = vxc
#    vyc = vyc
#    vzc = vzc
    xc = float(xc)/N
    yc = float(yc)/N
    zc = float(zc)/N
    vxc = float(vxc)/N
    vyc = float(vyc)/N
    vzc = float(vzc)/N
#    print xc, yc, zc, vxc, vyc, vzc

    t = 0.0
    dant = getDistance(xc, yc, zc)
    t = 1.0
    dmedio = getDistance(xc + vxc*t, yc + vyc*t, zc + vzc*t)
    if (abs(dant - dmedio) < ERROR):
        dmin = dmedio 
        tmin = 0.0
    else:
        while True:
            t += 1.0
            dpos = getDistance(xc + vxc*t, yc + vyc*t, zc + vzc*t)
            if (dpos > dmedio):
                if (dpos > dant):
                    dmin, tmin = calcula(t-2, t-1, dant, dmedio, xc, yc, zc, vxc, vyc, vzc)
                else:
                    dmin, tmin = calcula(t-1, t, dmedio, dpos, xc, yc, zc, vxc, vyc, vzc)
                break
            else:
                dant, dmedio = dmedio, dpos

#    print 'Restul = %s, %s' % (dmin, tmin)
#    print 'Case #%s: %.8f %.8f' % (case + 1, (dmin**0.5)/N, tmin)
#    print 'Case #%s: %.8f %.8f' % (case + 1, dmin**0.5, tmin)
    print 'Case #%s: %.8f %.8f' % (case + 1, dmin, tmin)


