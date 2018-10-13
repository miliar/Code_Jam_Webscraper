import sys
from itertools import *

def release(start, stop, to_release):
    if not to_release:
        return 0
    assert start <= stop, to_release

    m = to_release.pop()
    print "releaseing" ,m, to_release, start,stop
    
    return (stop-start +
            release(start, m-1, [x for x in to_release if x < m ]) +
            release(m+1, stop, [x for x in to_release if x > m ]))
    
def solve(input, case_no):
    print "solving ", case_no
    P, _ = map(int, input.next().strip().split())
    to_release = list(sorted(map(int, input.next().strip().split())))
    
    vals=[release(1, P, list(release_order)) for release_order in permutations(to_release)]
       
    rval = min(vals)
    print rval
    return rval
    
input = iter(open(sys.argv[1], 'r'))
output = open(sys.argv[1].replace('.in', '.out'), 'w')

T = int(input.next().strip())

for case_no in range(T):
    solution = solve(input,case_no)
    print >>output, "Case #%d: %s"  % (case_no+1, solution) 