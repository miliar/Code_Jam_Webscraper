import sys

T = int(sys.stdin.readline().strip())


for i in xrange(T):
    r1 = int(sys.stdin.readline().strip())
    a1 = []
    for j in xrange(4):
        row = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        a1.append(row)

    r2 = int(sys.stdin.readline().strip())
    a2 = []
    for j in xrange(4):
        row = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        a2.append(row)

    v = set(a1[r1-1]).intersection(set(a2[r2-1]))

    if len(v) > 1:
        output = "Bad magician!"
    elif len(v) == 1:
        output = str(list(v)[0])
    else:
        output = "Volunteer cheated!"

    print "Case #%d: %s" % (i+1,  output)



    
