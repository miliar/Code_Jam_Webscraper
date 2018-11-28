import sys

input = sys.stdin
L, D, N = map(int, input.readline().split())

words = []
for i in xrange(D):
    words.append(input.readline())

words.sort()
words2 = dict((w, True) for w in words)

def tokenize(line):
    res = []

    in_paren = False
    for c in line:
        if not in_paren:
            if c != '(':
                res.append(c)
            else:
                in_paren = True
                res.append([])
        else:
            if c != ')':
                res[-1].append(c)
            else:
                in_paren = False
    return res


test_cases = map(tokenize, input.readlines())

def count_words(test_case):
    possible = words
    for c, token in enumerate(test_case):
        if type(token) == list:
            possible = filter(lambda w: w[c] in token, possible)
        else:
            possible = filter(lambda w: w[c] == token, possible)
        if not possible: return 0
    return len(possible)

def process_case(case, i):
    num = count_words(case)
    print "Case #%d: %d" % (i + 1, num)


for i, test_case in enumerate(test_cases):
    process_case(test_case, i)


