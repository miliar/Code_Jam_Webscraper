import sys

f = open(sys.argv[1])

n = int(f.readline())

for t in xrange(0,n):
    A = set()
    B = set()
    line = int(f.readline())
    for i in range(1,5):
        l = f.readline().strip("\n")
        if i == line:
            for x in l.split(" "):
                A.add(x)

    row = int(f.readline())
    for i in range(1,5):
        l = f.readline().strip("\n")
        if i == row:
            for x in l.split(" "):
                B.add(x)


    C = A & B

    if len(C) == 0:
        print "Case #%d: Volunteer cheated!" % (t+1)
    elif len(C) > 1:
        print "Case #%d: Bad magician!" % (t+1)
    else:
        s = C.pop()
        print "Case #%d: %s" % (t+1, s)










