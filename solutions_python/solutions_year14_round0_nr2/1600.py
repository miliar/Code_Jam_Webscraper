with open('B-large.in', 'r') as f:
    with open('a.out', 'w') as w:
        t = int(f.readline())
        for i in xrange(t):
            s = f.readline().split()
            C, F, X = float(s[0]),float(s[1]),float(s[2])
            c, p, sec = 0.0, 2.0, 0.0
            if C > X:
                sec = X/p
            else:
                while c < X:
                    sec += C/p
                    c += C
                    if (X-c)/p > X/(p+F):
                        c -= C
                        p += F
                    else:
                        sec += (X-c)/p
                        break
            w.write("Case #%i: %.7f\n" % (i+1, sec))
