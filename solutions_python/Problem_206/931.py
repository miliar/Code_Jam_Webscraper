T = int(raw_input(""))

for o in range(1, T+1):
    D, N = [int(x) for x in raw_input("").split(" ")]
    H = []
    time = -1000000000000000000000000
    for i in range(N):
        p, s = [int(x) for x in raw_input("").split(" ")]
        _time = ((float)(D-p))/s
        time = max([time, _time])

    res = D / time

    print "Case #%d: %.6f" % (o, res)
