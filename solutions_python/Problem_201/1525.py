# Bathroom Stall program
#Written by John Schroder  johnschroder@gmail.com
import operator

def calc(n, k):
    if k == 0:
        return n,n
    if k == 1:
        return n/2, (n-1)/2
    stallcount = {n: 1}
    maxS = n
    iter = 0
    while k > 0:
        iter += 1
        n = min(k,stallcount[maxS])
        k -= n
        s0 = maxS/2
        s1 = (maxS-1)/2
        stallcount[s0] = stallcount.get(s0,0) + n
        stallcount[s1] = stallcount.get(s1,0) + n
        stallcount[maxS] -= n
        if stallcount[maxS] == 0:
            del stallcount[maxS]
            maxS =max(stallcount.keys())

    return max(s0,s1), min(s0,s1)


def process(inputfilename, outputfilename):
    fin = open(inputfilename, "r")
    fout = open(outputfilename, "w")

    t = int(fin.readline());
    caseNumber = 0
    while t > 0:
        caseNumber += 1
        t -= 1
        line = fin.readline()
        tokens = line.split(" ")
        n = int(tokens[0])
        k = int(tokens[1])
        maxS, minS = calc(n,k)
        fout.write("Case #%d: %d %d\n" % (caseNumber, maxS, minS))


process("test.in", "test.out")
print "done"