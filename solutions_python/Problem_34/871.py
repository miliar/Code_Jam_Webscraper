import sys

def parse(pat):
    if '(' not in pat:
        return list(pat)

    p = [d.split(')') for d in pat.split('(') if d]
    p2 = []
    for x in p:
        for k in x:
            if k and x.index(k) == 1:
                for l in k:
                    p2.append(l)
            elif k:
                p2.append(k)

    return p2

assert parse("(ab)d(dc)") == ['ab', 'd', 'dc']
assert parse("(zyx)bc") == ['zyx', 'b', 'c']
assert parse("(abc)(abc)(abc)") == ['abc', 'abc', 'abc']
assert parse("(ab)(bc)(ca)") == ['ab', 'bc', 'ca']
assert parse('abc') == ['a', 'b', 'c']


def rec_match(pat, words, L):
    p = parse(pat)
    matches = 0

    for w in words:
        for i in range(len(w)):
            if w[i] not in p[i]:
                break
            elif i == len(w) - 1:
                matches += 1

    return matches


(L, D, N) = [int(d) for d in sys.stdin.readline().strip('\n').split(' ')]
words = [sys.stdin.readline().strip('\n') for i in range(D)]

for k in range(1, N + 1):
    case = sys.stdin.readline().strip('\n')
    print 'Case #%d: %d' % (k, rec_match(case, words, L))
