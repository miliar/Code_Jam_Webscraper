from collections import defaultdict
import math

def get_l_and_r(n):
    x = float(n)
    l = int(max(0, math.ceil(x / 2) - 1))
    r = int(math.floor(x / 2))
    return (l, r)

with open("bathroom_stalls.small2", 'r') as f:
    lines = f.read().strip().split('\n')
    testcases = int(lines[0])
    for case in xrange(1, testcases + 1):
        gaps = defaultdict(int)
        tokens = map(int, lines[case].split(' '))
        n = tokens[0]
        k = tokens[1]
        gap_size = n
        gaps[gap_size] = 1
        max_gap_size = gap_size
        while k > 0:
            max_gap_size = max(gaps.keys())
            multiplicity = gaps[max_gap_size]
            l, r = get_l_and_r(max_gap_size)
            #print l, r
            #print gaps
            gaps[l] += multiplicity
            gaps[r] += multiplicity
            del gaps[max_gap_size]
            k -= multiplicity
        l, r = get_l_and_r(max_gap_size)
        print("Case #%s: %s %s" % (str(case), str(max(l, r)), str(min(l, r))))
