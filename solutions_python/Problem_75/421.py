import sys


T = int(input())
for testno in xrange(1, T + 1):
    data = sys.stdin.readline().split()
    C = int(data[0])
    D = int(data[C + 1])
    N = int(data[C + D + 2])

    combo = {}
    for i in xrange(C):
        c = data[i + 1]
        combo[c[0:2]] = c[2]
        combo[c[1::-1]] = c[2]

    opposes = set([])
    for i in xrange(D):
        op = data[i + C + 2]
        opposes.add(op)
        opposes.add(op[::-1])

    #print combo
    #print opposes
    #print data[-1]
    
    result = ''
    for i in xrange(N):
        elem = data[-1][i]
        if not result:
            result = elem
            continue

        if combo.has_key(result[-1] + elem):
            result = result[0:-1] + combo[result[-1] + elem]
            continue

        for e in result:
            if (e + elem) in opposes:
                result = ''
                break

        if result:
            result = result + elem

    print 'Case #{0}: [{1}]'.format(testno, ', '.join(result))
