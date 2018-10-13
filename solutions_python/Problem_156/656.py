import sys

def get_time(l, m):
    i = 0
    tt = 0
    while i < len(l) and l[i] > m:
        q, r = divmod(l[i], m)
        tt += q - 1 + (1 if r else 0)
        l.append(m if q else r)
        l[i] = 0
        i += 1
    tt += max(l)
    return tt

def solve(case):
    rcase = sorted(map(int, case[1].split()), reverse=True)
    best = rcase[0]
    for max_panq in range(best, 1, -1):
        this_time = get_time([x for x in rcase], max_panq)
        best = min(best, this_time)
    return best

def read_case(nlines):
    cases = int(sys.stdin.readline())
    for case in range(1, cases + 1):
        case_lines = [sys.stdin.readline().strip() for i in range(nlines)]
        yield [case, case_lines]

for case in read_case(2):
    print 'Case #{0}: {1}'.format(case[0], solve(case[1]))
