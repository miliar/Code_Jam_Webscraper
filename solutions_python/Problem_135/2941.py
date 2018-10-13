import sys

with file(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for i in range(T):
        r1 = int(f.readline().strip()) - 1
        rows1 = []
        for j in range(4):
            rows1.append([int(n) for n in f.readline().strip().split()])
        r2 = int(f.readline().strip()) - 1
        rows2 = []
        for j in range(4):
            rows2.append([int(n) for n in f.readline().strip().split()])
        selection = set(rows1[r1]).intersection(set(rows2[r2]))
        if len(selection) == 1:
            print "Case #%d: %d" % (i+1, list(selection)[0])
        elif len(selection) > 1:
            print "Case #%d: Bad magician!" % (i+1)
        else:
            print "Case #%d: Volunteer cheated!" % (i+1)
