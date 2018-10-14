
import sys

def line():
    return sys.stdin.readline().rstrip("\r\n")

def testcase():
    S = int(line())
    engines = frozenset(line() for i in xrange(S))
    Q = int(line())
    count = 0
    available = set(engines)
    for q in (line() for i in xrange(Q)):
        available.discard(q)
        if not available:
            count += 1
            available = set(engines)
            available.discard(q)
    return count

def main():
    n_cases = int(line())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %d" % (t_case, testcase())

if __name__ == "__main__":
    main()
