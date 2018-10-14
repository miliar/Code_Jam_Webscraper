import re

f = open('A-large.in')

lines = [line.strip('\n') for line in f.readlines()]

L, D, N = [int(i) for i in lines.pop(0).split()]

words = lines[:D]

test_cases = lines[D:]

p1 = re.compile('\([a-z]+\)|[a-z]')
for case, case_number in zip(test_cases, range(len(test_cases))):
    matches = 0
    m1 = re.findall(p1, case)
    m1 = [m.strip('()') for m in m1]
    for w in words:
        score = 0
        for m,i in zip(m1,range(len(m1))):
            if w[i] in m:
                score += 1

        if score == L:
            matches += 1
    print 'Case #%i: %i'%(case_number+1,matches)


