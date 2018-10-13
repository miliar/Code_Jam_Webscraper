import math
T = int(raw_input())

def sumtuple (a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def mult(t, n):
    return (t[0] * n, t[1] * n, t[2] * n)

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def sqrnorm(a):
    return dot(a, a)

def norm(a):
    return math.sqrt(sqrnorm(a))

def sumlist(L):
    S = (0, 0, 0)
    for a in L:
        S = sumtuple(S, a)
    return S

for t in xrange(T):
    N = int(raw_input())
    fliesPos = []
    fliesVel = []
    for x in range(N):
        f = [float(_) for _ in raw_input().split()]
        fliesPos.append((f[0], f[1], f[2]))
        fliesVel.append((f[3], f[4], f[5]))
    
    pos = mult(sumlist(fliesPos), 1.0/float(N))
    vel = mult(sumlist(fliesVel), 1.0/float(N))
    
    if norm(vel) > 0.0000001:
        dist = norm(cross(pos, vel)) / norm(vel)
        time = dot(pos, vel) / (norm(vel) * norm(vel))
    else:
        time = 0.0
        dist = norm(pos)
    
    if time >= 0:
        time = 0.0
        dist = norm(pos)
    else:
        time = abs(time)
    
    print "Case #"+str(t+1) + ": " + str(dist) + ' ' + str(time)
