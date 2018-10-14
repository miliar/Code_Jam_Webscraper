def parse(name):
    in_file = open('%s.in' % name, 'r')
    cases = int(in_file.readline())
    lines = []
    for case in range(cases):
        a, b, k = in_file.readline().split()
        solution = solve(int(a), int(b), int(k))
        line = 'Case #%s: %s' % (case + 1, solution)
        print line
        lines.append(line)
    in_file.close()
    out_file = open('%s.out' % name, 'w')
    out_file.write('\n'.join(lines))
    out_file.close()

def solve(a, b, k):
    cache = {}
    result = 0
    for ia in range(0, a):
        for ib in range(0, b):
            a_and_b = ia & ib
            cached = cache.get(a_and_b)
            if cached:
                result += cached
            else:
                sub_result = 0
                for ik in range(0, k):
                    if ik == a_and_b:
                        sub_result += 1
                cache[a_and_b] = sub_result
                result += sub_result
    return result

parse('B-small-attempt1')
