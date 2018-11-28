import fileinput

test = [line.rstrip() for line in fileinput.input()]
cases = int(test[0])
for i in range(cases):
    row1 = int(test[i*10+1])
    row2 = int(test[i*10+6])
    one = test[i*10+row1+1].split(" ")
    two = test[i*10+row2+6].split(" ")
    possible = filter(lambda x: x in two, one)
    if len(possible) == 1:
        print "Case #%d: %s" % (i+1, possible[0])
    elif len(possible) > 1:
        print "Case #%d: Bad magician!" % (i+1)
    else:
        print "Case #%d: Volunteer cheated!" % (i+1)