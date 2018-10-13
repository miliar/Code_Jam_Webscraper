import sys, itertools, re, operator

def partition(lst, n):
    division = len(lst) / float(n)
    return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n)]

def get_input():
    with open(sys.argv[1]) as f:
        lines = f.readlines()[1:]

    data = []
    for l, line in partition(lines, len(lines) / 2):
        tokens = map(int, line.split())
        data.append(tokens)
    return data

def solve(case):
    m = 0
    s = set([])
    for x in range(1, len(case)/2 + 1):
        s |= set(itertools.combinations(case, x))

    # print s

    for a in s:
        b = case[:]
        for x in a:
            b.remove(x)
        if reduce(operator.xor, a, 0) == reduce(operator.xor, b, 0):
            m = max(m, *map(sum, (a, b)))
    if m == 0:
        return 'NO'
    return m

data = get_input()
# print data

for idx, case in enumerate(data):
    print ("Case #%s: %s" % (idx+1, solve(case))).replace("'", '')
