t = int(raw_input())
for i in range(t):
    a = int(raw_input())-1
    for j in range(4):
        r = raw_input()
        if j == a:
            row1 = [int(x) for x in r.split(' ')]
    a = int(raw_input())-1
    for j in range(4):
        r = raw_input()
        if j == a:
            row2 = [int(x) for x in r.split(' ')]

    same = set(row1).intersection(set(row2))
    same = list(same)
    if len(same) == 1:
        print "Case #%d: %d" % (i+1, same[0])
    elif len(same) == 0:
        print "Case #%d: %s" % (i+1, "Volunteer cheated!")
    else:
        print "Case #%d: %s" % (i+1, "Bad magician!")

        
