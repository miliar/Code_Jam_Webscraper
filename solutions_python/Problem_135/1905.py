import sys, string

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()

for t in range(T):
    a = readint()
    
    for i in range(a):
        na = readlist()
    for i in range(4-a):
        readlist()
    
    b = readint()
    for i in range(b):
        nb = readlist()
    for i in range(4-b):
        readlist()
    
    nc = list(set(na) & set(nb))
    
    if len(nc) == 1:
        print "Case #%d: %d" % (t+1, nc[0])
    elif len(nc) > 1:
        print "Case #%d: Bad magician!" % (t+1)
    else:
        print "Case #%d: Volunteer cheated!" % (t+1)
