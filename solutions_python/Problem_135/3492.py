__author__ = 'Gibi'

f = open("small.txt")
num_tc = int(f.readline().strip())
for tc in range(1, num_tc + 1):
    answer_set = set()
    row = int(f.readline().strip())
    for r in range(1, 5):
        line = f.readline().strip()
        if r == row:
            answer_set |= set(line.split())
    col = int(f.readline().strip())
    for c in range(1, 5):
        line = f.readline().strip()
        if c == col:
            answer_set &= set(line.split())
    if len(answer_set) == 0:
        print "Case #%d: Volunteer cheated!" % tc
    elif len(answer_set) == 1:
        print "Case #%d: %s" % (tc, list(answer_set)[0])
    else:
        print "Case #%d: Bad magician!" % tc

