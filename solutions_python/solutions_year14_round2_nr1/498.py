__author__ = 'cni'

import os

def getCore(s):
    res = []

    prev_char = None
    for i in xrange(len(s)):
        if prev_char != s[i]:
            res.append(s[i])
            prev_char = s[i]

    return ''.join(res)

def getPart(s, c):
    res = []
    for i in xrange(len(s)):
        if s[i] == c:
            res.append(c)
        else:
            return (len(res), s[i:])
    return (len(res), s[i:])

def ccal(counts):
    min_cost = 101

    for i in counts:
        cost = 0

        for j in counts:
            cost += abs(i - j)
        if min_cost > cost:
            min_cost = cost
    return min_cost

def cal(strs):
    core = getCore(strs[0])

    for i in xrange(1, len(strs)):
        if core != getCore(strs[i]):
            return 'Fegla Won'

    cost = 0

    for i in xrange(len(core)):
        c = core[i]

        new_strs = []
        counts = []

        #print strs, c, i
        for j in xrange(len(strs)):
            x ,y = getPart(strs[j], c)
            counts.append(x)
            new_strs.append(y)
        #print new_strs, counts
        strs = new_strs
        cost += ccal(counts)

    return str(cost)


folder = '/Users/cni/Downloads'
file = os.path.join(folder, 'A-small-attempt0.in.txt')
f = open(file)
lines = f.readlines()
f.close()

N = int(lines[0])
idx = 1

for case_num in xrange(1, N + 1):
    print 'Case #%d:' % case_num,

    n = int(lines[idx])
    idx += 1

    strs = []
    for i in xrange(n):
        strs.append(lines[idx].strip())
        idx += 1

    res = cal(strs)

    print res
