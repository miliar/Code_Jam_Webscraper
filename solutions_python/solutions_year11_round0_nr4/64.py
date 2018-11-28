T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    N = int(raw_input());
    List = map(int, raw_input().split());
    TODO = 0;
    for i in range(N):
        if List[i] != i+1:
            TODO += 1;
    print "%5f" % TODO
