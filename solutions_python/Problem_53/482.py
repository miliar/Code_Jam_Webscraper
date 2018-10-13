import sys

def readInput(inputFile):
    f = open(inputFile)
    n = int(f.readline())
    cases = []
    for l in f.readlines():
        n, k = l.split()
        cases.append((int(n), int(k)))
    f.close()
    return cases

def binListToInteger(s):
    i = 0
    l = list(s)
    l.reverse()
    for t in l:
        i *= 2
        i += t
    return i

def calculateFinalState(n, k):
    a = 1 << n
    s = (a - 1) == (k % a)
    return s

def snapperChain(inputFile):
    data = readInput(inputFile)
    i = 1
    for d in data:
        c = 'ON' if calculateFinalState(d[0], d[1]) else 'OFF'
        print 'Case #%i: %s' % (i, c)
        i += 1  

if __name__ == '__main__':
    if len(sys.argv) > 1:
        snapperChain(sys.argv[1])