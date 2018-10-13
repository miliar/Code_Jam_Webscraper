import re
import numpy as np

#f = open('B-test.in')
#f = open('B-small.in')
f = open('B-large.in')

lines = [line.strip('\n') for line in f.readlines()]
T = int(lines.pop(0))

def pop_lines(list, N):
    ret = []
    for i in range(N):
        ret.append(list.pop(0))
    return ret


for k in range(T):
    N = int(lines.pop(0))
    flies = pop_lines(lines,N)

    xyz = np.zeros(3)
    vxvyvz = np.zeros(3)
    for fly in flies:
        fly = fly.split(' ')
        xyz += np.array([int(i) for i in fly[:3]])
        vxvyvz += np.array([int(i) for i in fly[3:]])
    t = -np.dot(xyz,vxvyvz)/(np.dot(vxvyvz,vxvyvz) or 1.0)
    if t < 10e-10:
        t = 0.0
    c = (xyz+vxvyvz*t)/N
    d = np.sqrt(np.dot(c,c))
    if abs(d) < 10e-10:
        d = 0.0

    print "Case #%d: %.8f %.8f"%(k+1,d,t)

f.close()
