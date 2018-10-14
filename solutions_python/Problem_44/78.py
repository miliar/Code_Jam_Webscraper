import fileinput
import sys
import math

def processInput():
    tcIn = fileinput.input()
    tcCount = int(tcIn.readline())
    for i in range(tcCount):
        N = int(tcIn.readline())
        flies = []
        for f in range(N):
            flies.append([int(x) for x in tcIn.readline().split()])
        dmin, tmin = findMin(flies)
        print "Case #%d: %.8f %.8f" % (i+1, dmin, tmin)

def distance(c):
    d = 0.0
    for i in c:
        d += i*i
    return math.sqrt(d)

def getC(flies):
    x,y,z,vx,vy,vz = [0.0 for _ in range(6)]
    N = len(flies)
    for f in flies:
        x += f[0]
        y += f[1]
        z += f[2]
        vx += f[3]
        vy += f[4]
        vz += f[5]
    return (x/N, y/N, z/N), (vx/N, vy/N, vz/N)

def findMinT(pc, vc):
    if vc[0] == vc[1] and vc[0] == vc[2] and vc[0] == 0:
        return 0.0
    t = -(pc[0]*vc[0]+pc[1]*vc[1]+pc[2]*vc[2]) / (vc[0]*vc[0]+vc[1]*vc[1]+vc[2]*vc[2])
    c = pc[0]*pc[0]+pc[1]*pc[1]+pc[2]*pc[2]
    b = 2*(pc[0]*vc[0]+pc[1]*vc[1]+pc[2]*vc[2])
    a = vc[0]*vc[0]+vc[1]*vc[1]+vc[2]*vc[2]
    k = b*b - 4*a*c

    if k>=0.0:
        t1 = (-b + math.sqrt(k))/2*a
        t2 = (-b - math.sqrt(k))/2*a
        t = min(t, t1, t2)
    if t < 0.0:
        t = 0.0
    return t

def findMinD(p, v, t):
    return distance((p[0]+v[0]*t, p[1]+v[1]*t, p[2]+v[2]*t))

def findMin(flies):
    pc, vc = getC(flies)
    #print pc, vc, distance(pc)

    t = findMinT(pc, vc)
    d = findMinD(pc, vc, t)
    return d, t

def main():
    processInput()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
