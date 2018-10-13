##
# CODEJAM
# prillan91
##
import sys


def solveSingle(f):
    temp = []

    data = f.readline().rstrip().split(' ')
    
    C = int(data[0])
    combines = data[1:C + 1]
    D = int(data[C + 1])
    opposites = data[C + 2:C + 2 + D]

    invokes = tuple(data[len(data) - 1])

    combines = [tuple(c) for c in combines]
    opposites = [tuple(d) for d in opposites]

    print data

    def combine(a, b):
        if a == '':
            return [a, b]
        for c in combines:
            if (c[0] == a and c[1] == b) or (c[1] == a and c[0] == b):
                return [c[2]]
        return [a, b]

    def hasopposite(a):
        for i in out + [last]:
            for c in opposites:
                if (c[0] == a and c[1] == i) or (c[1] == a and c[0] == i):
                    return True
        return False

    def add(a):
        if not a == '':
            out.extend([a])
    
    out = []
    last = ''
   
    for c in invokes:
        comb = combine(last, c)
        if len(comb) == 1:
            add(comb[0])
            last = ''
        elif hasopposite(c):
            out = []
            last = ''
        else:
            add(last)
            last = c
    add(last)
    return str(out).replace("'", '')






def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)) + "\n")
        


solve()
