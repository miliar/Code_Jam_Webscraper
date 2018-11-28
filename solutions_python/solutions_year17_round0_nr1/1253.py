"""

"""

import sys
with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    test_cases = [(list(s[0]), int(s[1])) for s in [s[:-1].split() for s in f.readlines()]]

#print(T)
#print('\n'.join(map(str, test_cases)))

flips = []
for s, k in test_cases:

    n_flips = 0
    # add left "stop"
    s.insert(0, '+')
    # check these pancakes
    ixs = range(1, len(s) - (k - 1))
    for ix in ixs:
        if s[ix - 1] == '+' and s[ix] == '-':
            # flip from left
            s[ix:ix + k] = [('+' if c == '-' else '-') for c in s[ix:ix + k]]
            n_flips += 1

    # check
    if all([c == '+' for c in s]):
        flips.append(str(n_flips))
    else:
        flips.append('IMPOSSIBLE')

t = 1
with open(sys.argv[2], 'w') as f:
    for flip in flips:
        f.write("Case #%d: %s\n" % (t, flip))
        t += 1
