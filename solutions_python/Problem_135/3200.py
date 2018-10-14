t = int(raw_input());

for i in xrange(t):
    r1 = int(raw_input());
    first_row = [];
    for j in xrange(4):
        if j == r1-1:
            first_row = raw_input().strip().split();
        else:
            a = raw_input();
    r2 = int(raw_input());
    second_row = [];
    for j in xrange(4):
        if j == r2-1:
            second_row = raw_input().strip().split();
        else:
            a = raw_input();    
    common = [];
    for j in xrange(4):
        if first_row[j] in second_row:
            common.append(first_row[j]);
    print "Case #{}:".format(str(i+1)),
    if len(common) == 0:
        print "Volunteer cheated!";
    elif len(common) == 1:
        print common[0];
    else:
        print "Bad magician!";
    
        
    
