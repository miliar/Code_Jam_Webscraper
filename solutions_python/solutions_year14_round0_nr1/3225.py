t = input()
def cardfinder():
    a1 = input()
    c1 = []
    for x in xrange(4):
        c1.append(map(int,raw_input().split()))
    a2 = input()
    c2 = []
    for x in xrange(4):
        c2.append(map(int,raw_input().split()))
    matches = []
    for x in c1[a1-1]:
        for y in c2[a2-1]:
            if x==y:
                matches.append(x)
    return matches

for x in xrange(t):
    matches = cardfinder()
    if (len(matches) == 0):
        print "Case #%d: Volunteer cheated!" %(x+1)
    if (len(matches) == 1):
        print "Case #%d: %d" %(x+1,matches[0])
    if (len(matches) > 1):
        print "Case #%d: Bad magician!" %(x+1)

        
