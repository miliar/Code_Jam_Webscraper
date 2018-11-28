import sys

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('jam1.out', 'w')
    t = int(f.readline())
    for test in xrange(1, t+1):
        str1 = "Case #%d: " %(test)
        output.write(str1)
        C, F, X = map(float, f.readline().split())
        time = 0.0
        rate = 2.0
        while (C/rate) + (X/(rate+F)) < X/rate:
            time = time + (C/rate)
            rate = rate + F
        time = time + (X/rate)
        output.write("%.7f\n" % time)

