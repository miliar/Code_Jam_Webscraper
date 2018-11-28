
nocases = int(raw_input());

for test_case in xrange(nocases):
    row_case_1 = int(raw_input());
    for i in xrange(row_case_1 - 1):
        raw_input();
    row_1 = set(raw_input().split());
    for i in xrange(4-row_case_1):
        raw_input();
    row_case_2 = int(raw_input());
    for i in xrange(row_case_2 - 1):
        raw_input();
    row_2 = set(raw_input().split());
    for i in xrange(4-row_case_2):
        raw_input();
    common = row_1.intersection(row_2);
    if (len(common) == 0):
        s = "Volunteer cheated!"
    elif (len(common) == 1):
        s = common.pop();
    else:
        s = "Bad magician!"

    print "Case #%d: %s" % ((test_case+1), s);

