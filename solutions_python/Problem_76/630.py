from itertools import combinations
import random
import sys

def write_small_test(filename):
    write_test(filename, 15)

def write_large_test(filename):
    write_test(filename, 1000)

def write_test(filename, n_max):
    f = open(filename, 'w')
    f.write('100\n')
    cases = []
    for _ in range(100):
        cases.append(generate_test_case(n_max))
    f.write('\n'.join(cases))
    f.close()

def generate_test_case(n_max):
    n = random.randint(2, n_max)
    result = '%d\n' % (n,)
    cs = []
    for n in range(n):
        cs.append(random.randint(1, 1000000))

    result += ' '.join([str(c) for c in sorted(cs)])
    return result

def parse_test_case(pieces, values):
    return sorted([int(v.strip()) for v in values.split()])

def patrick_sum(values):
    sum = 0
    for v in values:
        sum = sum ^ v

    return sum

def longrange(end):
    i = 0L
    while i<end:
        yield i
        i += 1L

def partitions(values):
    if not values:
        yield []
        return
    for i in longrange(2**len(values)/2):
        parts = [set(), set()]
        for item in values:
            parts[i&1].add(item)
            i >>= 1
        if not parts[0] or not parts[1]:
            continue
        yield parts

def run_test_case(values):
    sean_shares = []
    combos = partitions(values)
    for c in combos:
        ps0 = patrick_sum(c[0])
        ss0 = sum(c[0])
        ps1 = patrick_sum(c[1])
        ss1 = sum(c[1])
        #print "c0: %s\nc1: %s\nps0: %s\nps1: %s" % (c[0], c[1], ps0, ps1)
        if ps0 == ps1:
            sean_shares.append(max([ss0,ss1]))

    return sean_shares and max(sean_shares) or 0

if __name__=='__main__':
    f = open(sys.argv[1], 'r')
    num_test_cases = int(f.readline())
    for i in range(num_test_cases):
        test_case = parse_test_case(f.readline(), f.readline())
        v = run_test_case(test_case)
        if v==0:
            v = 'NO'
        print 'Case #%d: %s' % (i+1, v)
    f.close()