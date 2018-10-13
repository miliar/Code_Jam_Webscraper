inputfile = file("b-small.in", "rb")
outputfile = file("b-small.out", "wb")
out_yes = "Case #%d: %d"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    count = 0
    A, B, K = parse_line()
    for a in xrange(A):
        for b in xrange(B):
            if a&b < K:
                count += 1
                
    print >>outputfile, out_yes % (ncase, count)