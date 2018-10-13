def Solve(data):
    for i in range(len(data)-1, 0, -1):
        if data[i] < data[i-1]:
            data[i-1] -= 1;
            for j in range(i, len(data)):
                data[j] = 9;

    return ''.join(map(str, data))

T = int(raw_input());
for q in range(T):
    limit = map(int, list(raw_input()));

    print "Case #%d:" % (q+1),;
    print int(Solve(limit));
