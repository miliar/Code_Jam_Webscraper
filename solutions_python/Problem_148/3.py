def reader(inFile):
    (n, x) = inFile.getInts()
    return (inFile.getInts(),x)

from fractions import gcd

def solver((sizes, capacity)):
    numdisks = [0] * (capacity + 1)
    for i in sizes:
        numdisks[i] += 1
    tot = 0
    for cap in xrange(capacity, 1, -1):
        for i in xrange(cap+1):
            scr = min(numdisks[i], numdisks[cap - i])
            if i == cap - i:
                scr /= 2
            numdisks[i] -= scr
            numdisks[cap - i] -= scr
            tot += scr
    return tot + sum(numdisks)

if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(reader, solver, "/Users/luke/gcj/2014/2/a/", "a").run()
