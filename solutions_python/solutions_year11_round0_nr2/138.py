#!/usr/bin/python

import sys


def solve(combine, oppose, string):
    stack = []
    # Could be optimized by keeping track of how many of each we have.
    for c in string:
        # print "Processing c=%s, stack is %s" % (c, stack)
        # Try combine:
        if len(stack) >= 1:
            result = combine.get((c, stack[-1]))
            if result:
                stack.pop()
                stack.append(result)
                continue

        # If not, try oppose:
        cleared = False
        for bad in oppose.get(c, []):
            if bad in stack:
                stack = []
                cleared = True
                break
        if cleared:
            continue

        # Finally, just add it.
        stack.append(c)

    # print "final stack:", stack
    # print
    return stack


if __name__ == "__main__":
    tests = int(sys.stdin.readline())
    for t in range(tests):
        line = sys.stdin.readline().split()
        # print line
        pos = 0

        n_combine = int(line[pos])
        pos += 1
        combine = {} # (source_1, source_2) -> result
        for i in range(n_combine):
            s = line[pos]
            pos += 1
            assert len(s) == 3
            s1, s2, d = s
            combine[(s1, s2)] = d
            combine[(s2, s1)] = d
        # print combine

        n_oppose = int(line[pos])
        pos += 1
        oppose = {} # symb -> [symb]
        for i in range(n_oppose):
            s = line[pos]
            pos += 1
            assert len(s) == 2
            s1, s2 = s
            oppose[s1] = oppose.get(s1, []) + [s2]
            oppose[s2] = oppose.get(s2, []) + [s1]
        # print oppose

        n_string = int(line[pos])
        pos += 1
        string = line[pos]
        pos += 1
        assert len(string) == n_string
        assert pos == len(line)

        result = solve(combine, oppose, string)
        print "Case #%d: [%s]" % (t + 1, ", ".join(result))
