import sys

def main():
    f = open(sys.argv[1])
    testCases = int(f.readline())
    
    for i in xrange(1, testCases + 1):
        l = f.readline()
        print "Case #%d: %s" % (i, solve(l))

def solve(line):
    xs = line.split()
    c = int(xs[0])
    d = int(xs[1 + c])
    n = int(xs[2 + c + d])

    combinations = {}
    for i in xrange(1, c + 1):
        a, b, toElement = xs[i]
        combinations[min(a, b) + max(a, b)] = toElement
    
    oppositions = set()
    for i in xrange(c + 2, c + d + 2):
        oppositions.add(min(xs[i]) + max(xs[i]))

    sequence = xs[-1]
    elemList = []
    for current in sequence:
        coll = False
        if len(elemList) > 0:
            last = elemList[-1]
            comb = min(current, last) + max(current, last)
            if comb in combinations:
                elemList.pop()
                elemList.append(combinations[comb])
            else:
                for e in elemList:
                    if min(e, current) + max(e, current) in oppositions:
                        coll = True
                        break
                if coll:
                    elemList = []
                else:
                    elemList.append(current)
        else:
            elemList.append(current)
    return "[" + ", ".join(elemList) + "]"

main()
