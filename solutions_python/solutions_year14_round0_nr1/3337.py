cases = int(raw_input())

for i in xrange(1,  cases + 1):
    first = int(raw_input())
    values1 = None
    for j in xrange(1, 5):
        line = raw_input()
        if j == first:
            values1 = [int(x) for x in line.split()]

    second = int(raw_input())
    values2 = None
    for j in xrange(1, 5):
        line = raw_input()
        if j == second:
            values2 = [int(x) for x in line.split()]

    equal = []
    for j in xrange(0, 4):
        if values1[j] in values2:
            equal.append(values1[j])

    res = 'Case #%d: ' % i
    if len(equal) > 1:
        res += 'Bad magician!'
    elif len(equal) == 0:
        res += 'Volunteer cheated!'
    else:
        res += str(equal[0])

    print res
