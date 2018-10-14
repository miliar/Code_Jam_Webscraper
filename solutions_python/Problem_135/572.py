#!/usr/bin/env pypy

# IN_FILE = 'samples.in'
IN_FILE = 'A-small-attempt0.in'
OUT_FILE = 'small.out'

fp = open(IN_FILE, 'r')

NUM_TESTS = int(fp.readline())
TESTS = []
for i in range(NUM_TESTS):
    ans1 = int(fp.readline())
    mat1 = []
    for j in range(4):
        row = [int(x) for x in fp.readline().strip().split()]
        mat1.append(tuple(row))
    mat1 = tuple(mat1)

    ans2 = int(fp.readline())
    mat2 = []
    for j in range(4):
        row = [int(x) for x in fp.readline().strip().split()]
        mat2.append(tuple(row))
    mat2 = tuple(mat2)
    TESTS.append({
        'ans1': ans1,
        'mat1': mat1,
        'ans2': ans2,
        'mat2': mat2
    })
fp.close()

# from pprint import pprint
# pprint(TESTS)

fp = open(OUT_FILE, 'w')
for i in range(NUM_TESTS):
    t = TESTS[i]
    ans1 = t['ans1']
    mat1 = t['mat1']
    ans2 = t['ans2']
    mat2 = t['mat2']

    res = set(mat1[ans1 - 1]) & set(mat2[ans2 - 1])
    if len(res) == 1:
        fp.write('Case #' + str(i + 1) + ': ' + str(res.pop()) + '\n')
    elif len(res) > 1:
        fp.write('Case #' + str(i + 1) + ': Bad magician!\n')
    elif len(res) == 0:
        fp.write('Case #' + str(i + 1) + ': Volunteer cheated!\n')
    else:
        assert False
fp.close()
