import sets
for n in xrange(int(raw_input())):
        c = int(raw_input())
        num1 = sets.Set((map(int, [raw_input() for i in xrange(4)][c-1].split(" "))))
        c2 = int(raw_input())
        num2 = sets.Set((map(int, [raw_input() for i in xrange(4)][c2-1].split(" "))))
        sect = num1.intersection(num2)
        if len(sect) == 1:
            print "Case #%d: %d" % (n+1, list(sect)[0])
        elif len(sect) > 1:
            print "Case #%d: Bad magician!" % (n+1)
        elif len(sect) == 0:
            print "Case #%d: Volunteer cheated!" % (n+1)
