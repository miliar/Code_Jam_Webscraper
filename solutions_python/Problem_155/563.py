import sys
stdin = sys.stdin

T = int(stdin.readline())
for icase in range(T):
    sm, string = stdin.readline().strip().split()
    shyness = map(int, list(string))

    up = shyness[0]
    rr = 0
    for i in range(1, len(shyness)):
        if up < i:
            rr += i - up
            up = i
        up += shyness[i]

    print "Case #%d: %d" % (icase+1, rr)
            
