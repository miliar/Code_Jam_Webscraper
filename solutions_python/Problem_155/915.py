__author__ = 'amolina'

if __name__ == "__main__":
    with open("A.in") as f:
        cnt = 0
        for line in f:
#            print line
            try:
                maxLevel, info = line.split()
                cnt += 1
                totPeople = 0
                neededPeople = 0
                for i in xrange(int(maxLevel) + 1):
                    atThisLevel = ord(info[i]) - ord('0')
                    if totPeople < i and atThisLevel > 0:
                        neededPeople += (i - totPeople)
                        totPeople += (i - totPeople)
                    totPeople += atThisLevel
                print "Case #%s: %s" % (cnt, neededPeople)
            except ValueError:
                pass