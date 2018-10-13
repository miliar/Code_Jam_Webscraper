import sys
with sys.stdin as f:
    T = int(f.readline().strip())
    for testcase in range(T):
        orig = f.readline().strip().split()[1]

        total = 0
        excess = 0
        for i in range(len(orig)):
            if total >= i:
                total += int(orig[i])
            else:
                if int(orig[i]) > 0:
                    excess += i - total
                    total += (i - total) + int(orig[i])

        print "Case #%d: %d" % (testcase + 1, excess)
