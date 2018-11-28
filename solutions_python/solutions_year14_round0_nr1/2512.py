cases = int(raw_input())
def getSet():
    g = int(raw_input()) - 1
    s = set([])
    for i in xrange(4):
        line = raw_input()
        if i == g:
            l = map(int, line.split(" "))
            for n in l: s.add(n)
    return s
for c in xrange(cases):
    s1 = getSet()
    s2 = getSet()
    s3 = s1.intersection(s2)
    if len(s3) == 0:
        print "Case #%d: Volunteer cheated!" % (c + 1)
    elif len(s3) > 1:
        print "Case #%d: Bad magician!" % (c + 1)
    else:
        print "Case #%d: %d" % (c + 1, s3.pop())

