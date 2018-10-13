import sys, re

# Read L, D, N
l, d, n = [int(x) for x in sys.stdin.readline().split()]

# Read rest of input
lines = sys.stdin.read().split('\n')

lexicon = lines[:d]
patterns = lines[d:d+n]

for pattern, case in zip(patterns, range(1, n + 1)):
    # Convert pattern to reg-ex
    pattern = re.compile(pattern.replace('(', '[').replace(')', ']'))
    print "Case #%d: %d" % (case, len([x for x in lexicon if re.match(pattern, x) is not None]))
