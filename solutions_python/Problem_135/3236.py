import sys

nc = int(sys.stdin.readline())

for i in range(1, nc + 1):
    r = int(sys.stdin.readline()) - 1
    for j in range(4):
        l = sys.stdin.readline()
        if j == r:
            fr = set(l.split())

    r2 = int(sys.stdin.readline()) - 1
    for j in range(4):
        l = sys.stdin.readline()
        if j == r2:
            sr = set(l.split())

    cc = fr & sr
    if len(cc) == 1:
        print "Case #%s: %s" % (i, list(cc)[0])
    elif cc:
        print "Case #%s: Bad magician!" % i
    else:
        print "Case #%s: Volunteer cheated!" % i
