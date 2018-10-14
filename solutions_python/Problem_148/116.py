T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),;

    [N,X] = map(int, raw_input().split());
    data = map(int, raw_input().split());
    data.sort();
    data.reverse();

    Discs = 0;
    while len(data) >= 2:
        Discs += 1;
        current = data.pop(0);

        space = X-current;
        doubled = False;
        for e in data:
            if ((not doubled) and (e <= space)):
                data.remove(e);
                doubled = True;
        
    print Discs + len(data);
        
