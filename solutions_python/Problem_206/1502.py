testCases = int(input())

for testCase in range(1, testCases + 1):
    l = raw_input()
    d, n = map(int, l.split(" "))
    
    maxt = -1
    for i in range(n):
        m = raw_input()
        k, s = map(int, m.split(" "))
        remaining = d-k
        time = float(remaining)/s
        if time > maxt:
            maxt = time

    print "Case #%d: %.6f" % (testCase, float(d)/maxt)