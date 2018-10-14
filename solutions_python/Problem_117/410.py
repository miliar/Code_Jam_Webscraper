# -*- coding: utf-8 -*-


def is_possible_pattern(lawn):
    for line in lawn:
        i = 0
        for square in line:

            is_possible_line = True if [] == [gt for gt in line if gt > square] else False
            if not is_possible_line:
                is_possible_column = True if [] == [gt for gt in [li[i] for li in lawn] if gt > square] else False

            if not is_possible_line and not is_possible_column:
                return False

            i += 1

    return True


test = []
lawn_set = []
t = int(input())
for i in xrange(0, t):
    [n, m] = raw_input().split(' ')
    [n, m] = [int(n), int(m)]
    test.append((n, m))
    current_lawn = []
    for j in xrange(0, n):
        current_lawn.append([ int(nb) for nb in raw_input().split(' ')])
    lawn_set.append(current_lawn)


i = 1
for lawn in lawn_set:
    if is_possible_pattern(lawn):
        print "Case #"+str(i)+": YES"
    else:
        print "Case #"+str(i)+": NO"
    i += 1
