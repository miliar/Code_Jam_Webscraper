

def solve_case(N, S, p, ts):
    if p == 0:
        return N
    if p == 1:
        return sum(1 for t in ts if t > 0)

    min_unsurprising_total = p + (p - 1) + (p - 1)
    min_surprising_total = p + (p - 2) + (p - 2)

    result = 0

    for t in ts:
        if t >= min_unsurprising_total:
            result += 1
        elif t >= min_surprising_total:
            if S:
                S -= 1
                result += 1

    return result

for i in xrange(int(raw_input())):
    case = map(int, raw_input().split())
    N, S, p = case[:3]
    print 'Case #%i: %i' % (i + 1, solve_case(N, S, p, case[3:]))
