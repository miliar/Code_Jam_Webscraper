#!/usr/bin/python3

from sys import argv

IMPOSSIBLE = 0
SURPRISING = 1
NOT_SURPRISING = 2
EITHER = 3

# If it is not possible for the best score to be best with total
# total points, return impossible. If the only way is for it to be
# surprising, return surprising. Otherwise, return not_surprising.
def possible(best, total):
    if total < best:
        return IMPOSSIBLE
    if 3 * best - 1 <= total:
        return NOT_SURPRISING
    elif total == 3 * best - 2:
        return EITHER
    elif 3 * best - 4 <= total <= 3 * best - 3:
        return SURPRISING
    else:
        return IMPOSSIBLE

infile = open(argv[1])
cases = int(infile.readline())
for i in range(cases):
    line = infile.readline()
    n, s, p, *t = list(map(int, line.split()))
    #print('n = {} s = {} p = {} t = {}'.format(n, s, p, t))
    surprising, not_surprising, either = 0, 0, 0
    for j in range(n):
        result = possible(p, t[j])
        if result == SURPRISING:
            surprising += 1
        elif result == NOT_SURPRISING:
            not_surprising += 1
        elif result == EITHER:
            either += 1
        #else:
        #    print('Impossible!')
    #print('not surprising {}  surprising {}  either {}'.format(not_surprising, surprising, either))
    if surprising > s:
        #print('Too many surprising!')
        surprising = s # Turn the extra surprising ones to impossible
    elif s - surprising > either:
        ... # print('Not enough either!')
    total = not_surprising + s + (either - (s - surprising))
    print('Case #{}: {}'.format(i + 1, total))
