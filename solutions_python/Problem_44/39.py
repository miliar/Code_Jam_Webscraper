import sys
import math

T = int(sys.stdin.readline())

for i in xrange(1,T+1):
    N = int(sys.stdin.readline())
    pos = [None]*N
    vel = [None]*N
    for x in xrange(0,N):
        li = map(int,sys.stdin.readline().strip().split())
        pos[x] = li[0:3]
        vel[x] = li[3:6]

    cpos = [sum([a[j] for a in pos])/float(len(pos)) for j in xrange(0,3)]
    v = [sum([a[j] for a in vel])/float(len(vel)) for j in xrange(0,3)]

    if v[0] == 0 and v[1] == 0 and v[2] == 0:
        t = 0
    else:
        t = -((v[0]*cpos[0]+v[1]*cpos[1]+v[2]*cpos[2])/
              (v[0]*v[0]+v[1]*v[1]+v[2]*v[2]))

    if t<0:
        t=0
        
    dist0 = math.sqrt(sum([a*a for a in cpos]))
    dist1 = math.sqrt(sum([(cpos[j]+v[j]*t)**2 for j in xrange(0,3)]))

    if dist1 >= 0 and dist1<dist0:
        print "Case #%d: %.9f %.9f" % (i,dist1,t)
    else:
        print "Case #%d: %.9f %.9f" % (i,dist0,0.0)
    
    
    #print t, cpos, math.sqrt(sum([x*x for x in cpos]))
