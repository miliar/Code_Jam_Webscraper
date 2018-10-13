#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[1] + ".out", 'wb')

if __name__ == "__main__":
    lines = infile.readlines()
    tests = int(lines[0])
    idx = 1
    for i in range(tests):
        ii = i + 1
        items1 = set(lines[idx+int(lines[idx])].strip().split(" "))
        items2 = set(lines[idx+5+int(lines[idx+5])].strip().split(" "))
#        print items1
#        print items2
        intersect = items1 & items2
#        print intersect
        cnt = len(intersect)
        if (cnt == 1):
            print "Case #%d: %s" % (ii, list(intersect)[0])
        elif cnt > 1:
            print "Case #%d: Bad magician!" % ii
        else:
            print "Case #%d: Volunteer cheated!" % ii
        idx += 10

    infile.close()
    outfile.close()
