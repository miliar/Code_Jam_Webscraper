#!/usr/bin/env python
fp = open('in.txt', 'rU')
lines = (line.rstrip("\n") for line in fp.xreadlines())
T = int(lines.next())   # number of test cases
for case_index in range(T):
    K = int(lines.next())
    swaps = 0
    print 'Case #%d:' % (case_index+1),
    min_row = [max(('1'+lines.next()).rindex('1') - 1, 0) for line_index in range(K)]
    for row in range(K):
        if min_row[row] > row:
            found = [subrow for subrow in range(row, K) if row >= min_row[subrow]][0]
            del min_row[found]
            min_row.insert(row+1, min_row[row])
            swaps += found - row
    print swaps
