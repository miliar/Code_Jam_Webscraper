import fileinput
import itertools

def solve(N, Pd, Pg):
    if Pg == 100 and Pd != 100:
        return 'Broken'
    if Pg == 0 and Pd != 0:
        return 'Broken'
    D = 1
    while D <= N:
        if Pd * D % 100 == 0:
            return 'Possible'
        D += 1
    return 'Broken'

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    N, Pd, Pg = [int(x) for x in readline().split()]
    answer = solve(N, Pd, Pg)
    print "Case #%d: %s" % (case_no+1, answer)
