import sys


def solve(engines, queries):
    numswitches = [0] * len(engines)
    for query in queries:
        for i, engine in enumerate(engines):
            switches = numswitches[:i] + numswitches[i + 1:]
            min_when_switching = min(switches) + 1
            if query == engine:
                numswitches[i] = min_when_switching
            else:
                numswitches[i] = min(min_when_switching, numswitches[i])
    return min(numswitches)

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    lines.reverse()
    num = int(lines.pop())
    cases = []
    for i in range(num):
        numengines = int(lines.pop())
        engines = []
        for j in range(numengines):
            engines.append(lines.pop())
        numqueries = int(lines.pop())
        queries = []
        for j in range(numqueries):
            queries.append(lines.pop())
        cases.append((engines, queries))

    for i, (engines, queries) in enumerate(cases):
        print "Case #%s: %s" % (i + 1, solve(engines, queries))


