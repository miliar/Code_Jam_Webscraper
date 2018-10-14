import sys


def turnpancakes(p,l):
    p = list(p)
    if '-' not in "".join(p):
        return 0
    for j in xrange(0, len(p)):
        if p[j] == '-':
            i = j
            break
    count = 0
    while i <= (len(p)-l):
        for j in xrange(i, i+l):
            p[j] = '+' if p[j] == '-' else '-'
        count += 1
        if '-' not in "".join(p):
            return count
        for j in xrange(i,len(p)):
            if p[j] == '-':
                i = j
                break
    return 'IMPOSSIBLE'

test_cases = 0
case = 0
for line in sys.stdin:
    if case == 0:
        test_cases = int(line)
        case += 1
        continue
    line = line.split()
    print "Case #" + str(case) + ": " + str(turnpancakes(line[0], int(line[1])))
    if case == test_cases:
        break
    case += 1