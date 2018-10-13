import sys

ncases = int(sys.stdin.readline())
for case in xrange(1,ncases+1):
    ans1 = int(sys.stdin.readline())
    row1 = []
    for row in xrange(1,5):
        rowstring = sys.stdin.readline().rstrip().split()
        if row != ans1:
            continue
        for entry in rowstring:
            row1.append(int(entry))
    ans2 = int(sys.stdin.readline())
    correct = 0
    message = ""
    for row in xrange(1,5):
        rowstring = sys.stdin.readline().rstrip().split()
        if row != ans2:
            continue
        for entry in rowstring:
            current = int(entry)
            if current in row1:
                if correct != 0:
                    message = "Bad magician!"
                    break
                correct = current
    if message=="":
        if correct == 0:
            message = "Volunteer cheated!"
        else:
            message = str(correct)
    print "Case #" + str(case) + ": " + message
