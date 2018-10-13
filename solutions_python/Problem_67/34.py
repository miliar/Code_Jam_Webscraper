import sys
f = open(sys.argv[1])
cases = int(f.readline())
MAXD = 110
for case in range(1,cases+1):
    R = int(f.readline())
    hasbac = [ [False] * MAXD for row in range(MAXD) ]
    bcount = 0
    for r in range(R):
        # substract 1 to make zero-based
        x1, y1, x2, y2 = [ int(v)-1 for v in f.readline().split() ] 
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if not hasbac[y][x]:
                    hasbac[y][x] = True
                    bcount += 1
    time = 0
    while bcount > 0:
        if False:
            print bcount
            for y in range(MAXD):
                print "".join(str(int(v)) for v in  hasbac[y])
            print ""

        # update in-place south->north and east->west
        for y in range(MAXD-1,-1,-1):
            for x in range(MAXD-1,-1,-1):
                hasnorth = y>0 and hasbac[y-1][x]
                haswest = x>0 and hasbac[y][x-1]
                if hasbac[y][x]:
                    if not (hasnorth or haswest):
                        hasbac[y][x] = False
                        bcount -= 1
                else:
                    if hasnorth and haswest:
                        hasbac[y][x] = True
                        bcount += 1
        time += 1

    print "Case #%d: %d" % (case,time)
