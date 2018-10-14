
engines = []

class Solve:
    
    def __init__(self, P, K, L, F):
        P = int(P)
        K = int(K)
        L = int(L)
        for i in xrange(len(F)):
            F[i] = int(F[i])
        F.sort()
        F.reverse()
        layout = []
        for i in xrange(K):
            layout.append(0)
        for i in xrange(len(F)):
            round = i / K + 1
            key = i % K
            layout[key] += F[i] * round
        total = 0
        for strokes in layout:
            total += strokes
        out(str(total)+ "\n")

def out(s):
    print s,
    fOut.write(s)

if __name__ == "__main__":
    name = "A-large"
    fIn = open(name + '.in','r')
    fOut = open(name + '.out','w')
    cases = int(fIn.readline().rstrip())
    for caseNumber in range(cases):
        out("Case #%d: " % (caseNumber + 1))
        (P, K, L) = fIn.readline().split()
        F = fIn.readline().split()
        Solve(P, K, L, F)
    fIn.close()
    fOut.close()