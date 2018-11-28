#!/usr/bin/python

DATASET = 'small'
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def solve(R, k, groups):
    income = []
    next_group = []
    for i in xrange(len(groups)):
        j = i
        income.append(0)
        free = k
        while free >= groups[j]:
            free -= groups[j]
            income[i] += groups[j]
            j += 1
            j %= len(groups)
            if j == i: break
        next_group.append(j)
    print income
    print next_group
    group = 0
    money = 0
    for i in xrange(R):
        money += income[group]
        group = next_group[group]
    return money

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
T = int(ifile.readline())
for i in xrange(T):
    line = ifile.readline().split(' ')
    R = int(line[0])
    k = int(line[1])
    N = int(line[2])
    groups = [int(a) for a in ifile.readline().split(' ')]
    assert(len(groups) == N)
    ofile.write('Case #%s: %s\n' % (i+1, str(solve(R,k,groups))))
ifile.close()
ofile.close()
