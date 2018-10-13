import fileinput
import itertools
import operator


def solve(cc):
    if reduce(operator.xor, cc) != 0:
        return "NO"
    out = []
    for l in range(1, len(cc)/2+1):
        for s in itertools.combinations(cc, l):
            p = list(cc)
            for i in s:
                p.remove(i)
            ss = sum(s)
            sp = reduce(operator.xor, s)
            pp = reduce(operator.xor, p)
            if sp == pp:
                out.append(max(ss, sum(p)))
    if not out:
        return "NO"
    return max(out)

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    count = int(readline())
    candies = [int(part) for part in readline().split()]
    answer = solve(candies)
    print "Case #%d: %s" % (case_no+1, answer)
