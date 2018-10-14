import sys

def main():
    argv = sys.argv[1:]
    if len(argv) < 2:
        print 'Usage: a.py inputfile outputfile'
        sys.exit(1)
    inputFile = open(argv[0],'rU')
    testCases = int(inputFile.readline().strip())
    result = []
    helper = {}
    for i in xrange(11):
        for j in xrange(3):
            for k in xrange(j, 3):
                t = (i, i+j, i + k)
                xt = 3 * i + j + k
                if i + j > 10 or i + k > 10:
                    continue
                iss = 0
                if j > 1 or k > 1:
                    iss = 1
                if xt not in helper:
                    helper[xt] = []
                helper[xt].append((t, iss))
                helper[xt] = sorted(helper[xt])
    for testCase in range(testCases):
        ln = inputFile.readline().strip().split()
        N = int(ln[0])
        S = int(ln[1])
        P = int(ln[2])
        tj = 0
        R = 0
        PR = 0
        for x in xrange(N):
            tj = int(ln[x + 3])
            htj = helper[tj]
            ptj = 0
            rtj = 0
            for h in xrange(len(htj)):
                hi = htj[h]
                tt = hi[0]
                if tt[0] >= P or tt[1] >= P or tt[2] >= P:
                    if hi[1] == 0:
                        rtj = 1
                    else:
                        ptj = 1
            if rtj == 1:
                R += 1
            elif ptj == 1:
                PR += 1
        R += min(PR, S)
        result.append('Case #%d: %d\n' % (testCase+1,R))
    outputFile = open(argv[1], 'w')
    outputFile.writelines(result)
    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    main()
