import sys, itertools


def solve():
    t = int(sys.stdin.readline().strip())
    for test_case in xrange(0, t):
        n = int(sys.stdin.readline().strip())
        l1s = list(map(float, sys.stdin.readline().strip().split(' ')))
        l2s = list(map(float, sys.stdin.readline().strip().split(' ')))

        def rule1(logs1, logs2):
            result = 0
            for l1 in list(logs1):
                l2 = min([i for i in logs2 if i >= l1]) if len([i for i in logs2 if i >= l1]) > 0 else min(logs2)
                if l1 > l2: result += 1
                logs2.remove(l2)
            return result

        rule1 = rule1(list(l1s), list(l2s))

        rule2 = 0
        while len(l1s) > 0:
            while len(l1s) > 0 and len([item for item in l1s if min(l2s) <= item <= max(l1s)]) > 0:
                r1 = min([item for item in l1s if min(l2s) <= item <= max(l1s)])
                r2 = min(l2s)
                l1s.remove(r1)
                l2s.remove(r2)
                rule2 += 1
            while len(l1s) > 0 and min(l2s) > min(l1s):
                r1 = min(l1s)
                r2 = max([item for item in l2s if item > min(l1s)])
                l1s.remove(r1)
                l2s.remove(r2)

        print >> sys.stdout, "Case #%s: %s %s" % (test_case + 1, rule2, rule1)


if __name__ == "__main__":
    solve()