f = open("C:/Users/Eric/dropbox/codejam/magic.in")

lines = f.readlines()[1:]
tests = [lines[x:x+10] for x in xrange(0, len(lines), 10)]

num = 1

for case in tests:
    result = set(case[int(case[0])].split()).intersection(set(case[int(case[5])+5].split()))
    if len(result) == 1:
        print "Case #%d: %s" % (num, list(result)[0])
    elif len(result) == 0:
        print "Case #%d: Volunteer cheated!" % (num)
    else:
        print "Case #%d: Bad magician!" % (num)
    num += 1
