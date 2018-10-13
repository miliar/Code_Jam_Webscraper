inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    X, R, C = parse_line()
    R, C = max(R, C), min(R, C)
    if R*C % X != 0:
        print >>outputfile, out_s % (ncase, "RICHARD")
        continue
    if X == 1:
        print >>outputfile, out_s % (ncase, "GABRIEL")
        continue
    if X == 2:
        print >>outputfile, out_s % (ncase, "GABRIEL")
        continue
    if X == 3:
        if R == 3 and C == 1:
            print >>outputfile, out_s % (ncase, "RICHARD")
            continue
        if R == 3 and C in (2, 3):
            print >>outputfile, out_s % (ncase, "GABRIEL")
            continue
        # Last case: R == 4 and C == 3
        assert R == 4 and C == 3
        print >>outputfile, out_s % (ncase, "GABRIEL")
        continue
    # X == 4
    if R == 2 and C == 2:
        print >>outputfile, out_s % (ncase, "RICHARD")
        continue
    # R == 4
    if C == 1:
        print >>outputfile, out_s % (ncase, "RICHARD")
        continue
    if C == 2:
        print >>outputfile, out_s % (ncase, "RICHARD")
        continue
    if C == 3:
        print >>outputfile, out_s % (ncase, "GABRIEL")
        continue
    if C == 4:
        print >>outputfile, out_s % (ncase, "GABRIEL")
        continue
    
        
        