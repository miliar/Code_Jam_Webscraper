def Solve(inp, size):
    flips = 0;

    data = [];    
    for c in inp:
        data.append(c == '+');

    for i in range(len(inp)-size+1):
        if (not data[i]):
            flips += 1;
            for j in range(size):
                data[i+j] = not data[i+j];

    if (False in data):
        return "IMPOSSIBLE";
    return flips;


T = int(raw_input());
for q in range(T):
    data = raw_input().split();
    sides = data[0];
    size = int(data[1]);

    print "Case #%d:" % (q+1),;
    print Solve(sides, size);
