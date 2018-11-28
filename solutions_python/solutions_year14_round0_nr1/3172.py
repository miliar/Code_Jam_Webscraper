def get_elements(f):
    where = int(f.readline())
    for i in range(where-1):
        f.readline()
    line = []
    for j in f.readline().split(' '):
        line.append(int(j))
    for i in range(4-where):
        f.readline()
    return set(line)

f = open("A-small-attempt1.in", 'r')
testcases = int(f.readline())
for i in range(testcases):
    line1 = get_elements(f)
    line2 = get_elements(f)
    a = set(line1).intersection(set(line2))
    if len(a) == 0:
        print "Case #%d: Volunteer cheated!" % (i+1)
    elif len(a) == 1:
        print "Case #%d: %d" % (i+1, a.pop())
    else:
        print "Case #%d: Bad magician!" % (i+1)
