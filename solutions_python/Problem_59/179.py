import sys

f = open(sys.argv[1])

T = int(f.readline())

def log(fmt, args):
    if False:
        print fmt % args

for case in range(1,T+1):
    N, M = [int(x) for x in f.readline().split()]
    total = 0
    tree = {'':{}}
    for pn in range(N):
        path = f.readline().strip()
        segs = path.split('/') 
        root = tree
        for seg in segs:
            if seg in root:
                root = root[seg]
            else:
                root[seg] = {}
                root = root[seg]
    for pm in range(M):
        path = f.readline().strip()
        segs = path.split('/')
        root = tree
        for seg in segs:
            if seg in root:
                root = root[seg]
            else:
                root[seg] = {}
                root = root[seg]
                log("Adding %s", seg)
                total += 1
    print 'Case #%d: %d' % (case, total)

