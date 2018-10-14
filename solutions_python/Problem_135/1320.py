import sys

f = open(sys.argv[1])

cases = int(f.readline())
for i in xrange(cases):
    a = int(f.readline())
    lines1 = []
    for j in xrange(4):
        l = f.readline()
        if (j == a - 1):
            lines1 = l

    lines2 = []
    b = int(f.readline())
    for j in xrange(4):
        l = f.readline()
        if (j == b - 1):
            lines2 = l
    card = set(lines1.split()).intersection(lines2.split())

    print "Case #" + str(i+1) + ":",
    if (len(card) == 1):
        print list(card)[0]
    elif (len(card) > 1):
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
