t = int(raw_input())

for ab in xrange(t):
    row1 = int(raw_input())
    mat1 = []
    for i in xrange(4):
        r = raw_input()
        a = []
        a = map(int, r.split())
        mat1.append(a)

    row2 = int(raw_input())
    mat2 = []
    for i in xrange(4):
        r = raw_input()
        a = []
        a = map(int, r.split())
        mat2.append(a)

    a = mat1[row1-1]
    b = mat2[row2-1]
    intersection = list(set.intersection(set(a),set(b)))
    print "Case #" + str(ab+1) + ":",
    if len(intersection) == 0:
        print "Volunteer cheated!"
    elif len(intersection) > 1:
        print "Bad magician!"
    else:
        print intersection[0]
