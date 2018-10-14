def minimize(f):
    minimum = f(0)
    tp = 1
    while f(tp) < minimum:
        minimum = f(tp)
        tp *= 2

    minimum = min([f(i) for i in xrange(0, tp + 1)])
    return minimum

def solveit():
    C, F, X = [float(x) for x in f.readline().split()]

    def tottime(n):
        t = 0.0
        for i in xrange(0, n):
            t += C / (2.0 + i * F)
        t += X / (2.0 + n * F)
        return t

    return minimize(tottime)

outfile = open("results.txt", "w")
with open("test.txt") as f:
    testcases = int(f.readline())

    for i in xrange(0, testcases):
        outcome = solveit()
        print "Case #%d:" % (i + 1,), outcome
        print >> outfile, "Case #%d:" % (i + 1,), outcome
