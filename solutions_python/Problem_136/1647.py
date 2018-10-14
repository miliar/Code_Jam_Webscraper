infile = open("B-small-attempt0.in", "rU")
outfile = open("B_small.out", "w")

ncases = int(infile.readline())

def f(n, X, C, F):
    total = 0

    for j in xrange(n):
        total += float(C)/(2 + j*F)

    total += float(X)/(2 + n*F)

    return total

for case in xrange(1, ncases+1):
    C, F, X = [float(x) for x in infile.readline().strip().split(" ")]

    minimum = float(X)/2

    n = 1

    while f(n, X, C, F) < minimum:
        minimum = f(n, X, C, F)
        n += 1

    outfile.write("Case #%d: %.10f\n" % (case, minimum))

outfile.close()
        
