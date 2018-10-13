__author__ = 'cni'

import os

def cal(A, B, K):
    count = 0
    for i in xrange(A):
        for j in xrange(B):
            if i & j < K:
                count += 1

    return count


folder = '/Users/cni/Downloads'
file = os.path.join(folder, 'B-small-attempt0.in.txt')
f = open(file)
lines = f.readlines()
f.close()

N = int(lines[0])
idx = 1

for case_num in xrange(1, N + 1):
    print 'Case #%d:' % case_num,

    A, B, K = [int(i) for i in lines[idx].split()]
    idx += 1

    res = cal(A, B, K)

    print res
