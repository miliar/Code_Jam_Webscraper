import sys

lines = sys.stdin.readlines()

cases = int(lines[0])

lines = lines[1:]

for t in range(cases):
    first_row = int(lines[0])
    first = map(int, lines[first_row].split())
    lines = lines[5:]
    second_row = int(lines[0])
    second = map(int, lines[second_row].split())
    common = [i for i in first if i in second]
    if (len(common) == 0):
        print "Case #%d: Volunteer cheated!" % (t+1)
    elif (len(common) == 1):
        print "Case #%d: %d" % (t+1, common[0])
    else:
        print "Case #%d: Bad magician!" % (t+1)
    lines = lines[5:]
