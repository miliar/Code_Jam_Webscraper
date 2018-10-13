import sys

T = int(sys.stdin.readline())

for t in range(T):

    answer1 = int(sys.stdin.readline())
    rows1 = []
    for i in range(4):
        rows1.append(set([int(x) for x in sys.stdin.readline().split()]))
    answer2 = int(sys.stdin.readline())
    rows2 = []
    for i in range(4):
        rows2.append(set([int(x) for x in sys.stdin.readline().split()]))

    row1 = rows1[answer1 - 1]
    row2 = rows2[answer2 - 1]

    intersection = row1 & row2
    if len(intersection) == 0:
        print "Case #%d: Volunteer cheated!" % (t + 1)
    elif len(intersection) == 1:
        print "Case #%d: %d" % (t + 1, intersection.pop())
    else:
        print "Case #%d: Bad magician!" % (t + 1)