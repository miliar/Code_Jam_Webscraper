#testcase = ["abc", "bca", "dac", "dbc", "cba"]

#pattern = ["(ab)(bc)(ca)", "abc", "(abc)(abc)(abc)", "(zyx)bc"]

import re

def test(pattern, string):
    pattern = pattern.replace("(", "[").replace(")", "]")
    m = re.search(pattern, string)
    #print pattern, string
    if m and m.group(0) == string:
        #print pattern, string
        return True

def solve():
    f = file("A-large.in", "r")
    lines = f.readlines()
    L, D, N = map(int, lines[0].split())
    testcase = []
    pattern = []
    for i in xrange(D):
        testcase.append(lines[i+1])
    for i in xrange(N):
        pattern.append(lines[i + D + 1])

    result = {}
    output = "Case #%d: %d\n"

    for p in pattern:
        index = pattern.index(p)
        result[index + 1] = 0
        for t in testcase:
            if test(p, t):
                result[index + 1] += 1

    outputFile = file("A-small.out", "w")
    outputFile.writelines([output % one for one in result.iteritems()])

solve()