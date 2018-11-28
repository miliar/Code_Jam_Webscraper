def solve(max_shyness, shynesses):
    solution = 0
    for i in xrange(len(shynesses)):
        if i > sum(shynesses[:i]):
            shynesses[i - 1] = 1
            solution += 1

    return solution

if __name__ == '__main__':
    lines = open('A-large.in', 'r').readlines()
    test_cases = int(lines[0])
    for i in xrange(1, len(lines)):
        a, b = lines[i].strip().split()

        print 'Case #%d: %d' % (i, solve(int(a), [int(b[i]) for i in xrange(len(b))]))