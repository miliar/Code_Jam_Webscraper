import sys
import itertools
from collections import Counter

f = open('recycled.in', 'r')

case = -1
for line in f:
    case += 1
    if case == 0:
        continue

    sys.stdout.write('Case #' + str(case) + ': ')

    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])

    digits = len(str(a))

    num_recycled = 0
    for combination in itertools.combinations(xrange(a, b+1), 2):
        recycled = False
        n = combination[0]
        m = combination[1]
        strn = str(n)
        strm = str(m)
        impossible = False
        for char in strn:
            if char not in strm:
                impossible = True
                break
        for char in strm:
            if char not in strn:
                impossible = True
                break
        if impossible:
            continue
        #cn = Counter(strn)
        #cm = Counter(strm)
        #if cn != cm:
        #    continue
        for test_size in xrange(1, digits):
            # Test a subset of this many digits from the back
            test = strn[-test_size:] + strn[0:-test_size]
            if test == strm:
                num_recycled += 1
                # Try to debug the off-by-1 on 4 digits
                #if digits == 4:
                #    print strn, strm
        
    print num_recycled
