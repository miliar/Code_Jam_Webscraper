#!/usr/bin/python

def read_tokens(line):
    for token in line.split():
        yield token

def solve(line):
    tokens = read_tokens(line)
    chars = 'QWERASDF'
    combines = dict((char, {}) for char in chars)
    opposes = dict((char, set()) for char in chars)
    C = int(tokens.next())
    for i in range(C):
        combine = tokens.next()
        combines[combine[0]][combine[1]] = combine[2]
        combines[combine[1]][combine[0]] = combine[2]
    D = int(tokens.next())
    for i in range(D):
        oppose = tokens.next()
        opposes[oppose[0]].add(oppose[1])
        opposes[oppose[1]].add(oppose[0])
    N = int(tokens.next())
    elements = tokens.next()
    result = []
    for element in elements:
        if result:
            if result[-1] in combines and element in combines[result[-1]]:
                result[-1] = combines[result[-1]][element]
                continue
            opposed = False
            for oppose in opposes[element]:
                if oppose in result:
                    result = []
                    opposed = True
                    break
            if not opposed:
                result.append(element)
        else:
            result.append(element)
    return ', '.join(result)

T = int(raw_input())
for i in range(T):
    print 'Case #%d: [%s]' % (i + 1, solve(raw_input()))
