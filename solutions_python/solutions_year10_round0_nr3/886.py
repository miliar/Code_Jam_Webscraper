import sys
import itertools

with open(sys.argv[1]) as file:
    lines = file.readlines()

tests = []

# Parse the tests
offset = int(lines[0])
params = itertools.islice(lines, 1, None, 2)
groups = itertools.islice(lines, 2, None, 2)
for p,g in itertools.izip(params, groups):
    runs, capacity, _ = map(int, p.split())
    groups = map(int, g.split())
    test = (runs, capacity, groups)
    tests.append(test)

def do_test(runs, capacity, groups):
    total = 0
    memoize = {}
    for r in xrange(runs):
        hash = tuple(groups)
        if hash in memoize:
            val, groups = memoize[hash]
            total += val
        else:
            c = capacity
            val = 0
            for i, g in enumerate(groups):
                if c >= g:
                    c = c - g
                    val += g
                else:
                    break
            next = groups[i:] + groups[:i]
            total += val
            memoize[hash] = (val, next)
            groups = next

    return total

for i, test in enumerate(tests):
    total = do_test(*test)
    print 'Case #%d: %d' % (offset + i + 1, total)

