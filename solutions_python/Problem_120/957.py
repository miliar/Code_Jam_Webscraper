import math

def process(r, t):
    #print r, t
    r = float(r)
    t = float(t)
    ret = -(2 * r - 1) * 0.25 + 0.5 * math.sqrt((2 * r - 1) * (2 * r - 1) * 0.25 + 2 * t)
    #print ret
    return int(ret)

f = open(r'in.txt', 'r')

line = f.readline()
N = int(line)
for idx in xrange(0, N):
    line = f.readline()
    arr = line.split()
    r = int(arr[0])
    t = int(arr[1])
    #print r, t
    print 'Case #%d: %d' % (idx + 1, process(r, t))
f.close()
