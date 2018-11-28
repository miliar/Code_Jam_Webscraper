f = open('in')
fo = open('out', 'w')

for T in range(int(f.readline())):
    print 'Case #%d:' % (T + 1),
    ans1 = int(f.readline())
    #print "ans1: ", ans1

    for i in range(1, 5):
        line = f.readline().strip()
        # #print i, ": ", line
        if(i == ans1):
            row1 = map(int, line.strip().split(" "))
            # print "   row1: ", row1

    ans2 = int(f.readline())
    #print "ans2: ", ans2

    for i in range(1, 5):
        line = f.readline().strip()
        if(i == ans2):
            row2 = map(int, line.strip().split(" "))
            #print "   row2: ", row2

    ans = 0
    bad_magician = False
    for e in row1:
        if(e in row2):
            if(ans != 0):
                bad_magician = True
                break
            ans = e
            # print "ans: ", ans

    if(bad_magician):
        print "Bad magician!"
    elif (ans == 0):
        print "Volunteer cheated!"
    else:
        print ans




