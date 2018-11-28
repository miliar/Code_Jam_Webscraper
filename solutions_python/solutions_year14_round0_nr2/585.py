import math
for n in xrange(int(raw_input())):
        C, F, X = map(float,raw_input().split(" "))
        N = max(0, int((F*X - 2*C)/(F*C) - 1))
        total = sum(float(C/(2 + i*F)) for i in xrange(N))
        truetotal1 = total + X/(2 + N*F)
        truetotal2 = total + C/(2 + N*F) + X/(2 + N*F + F)
        truetotal3 = total + X/(2 + N*F - F) - C/(2 + N*F - F) if N > 0 else X
        print "Case #%d: %.7f" % (n+1, min(truetotal1, truetotal2))
