from sets import Set;
T = int(raw_input());

for t in range(1,T+1):
    row = int(raw_input())-1

    for r in range(4):
        line = raw_input();
        if (r == row) :
            a = Set(line.split());

    row = int(raw_input()) -1
    for r in range(4):
        line = raw_input();
        if (r == row) :
            b = Set(line.split())

    if(len(a.intersection(b)) == 0):
         print "Case #%s: Volunteer cheated!" % t
    elif (len(a.intersection(b)) == 1):
        print "Case #%s: %s" %(t, list(a.intersection(b))[0]);
    else:
        print "Case #%s: Bad magician!" % t 
