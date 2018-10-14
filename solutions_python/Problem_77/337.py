def not_in_place(a):
    so = sorted(a);
    not_ints = [];
    for i in xrange(len(a)):
        if a[i] != so[i]:
            not_ints.append(a[i]);
    return not_ints;

cases = int(raw_input());
for cur_case in xrange(cases):
    raw_input();
    array = map(int,raw_input().split());
    prob = len(not_in_place(array));
    print "Case #%d: %f" % (cur_case+1,prob);
