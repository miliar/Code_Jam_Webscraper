from __future__ import division

'''
def sub(matrix, i):
    indices = set([j for j,c in enumerate(matrix[i]) if c!='.'])
    rows = [row for j,row in enumerate(matrix) if j in indices]
    return [[c for j,c in enumerate(row) if j in indices] for row in rows]
'''

def wp(matrix, i):
    ones = matrix[i].count('1')
    zeros = matrix[i].count('0')
    if ones + zeros == 0:
        return 0
    return ones / (ones + zeros)

def owp(matrix, i):
    sub_matrix = [r[:i]+r[i+1:] for j,r in enumerate(matrix) if j!=i]
    wps = sum(wp(sub_matrix, j) if j<i else wp(sub_matrix, j-1) for j in range(len(matrix)) if matrix[i][j]!='.')
    return wps / (len(matrix) - matrix[i].count('.'))

def oowp(matrix, i):
    indices = set([j for j,c in enumerate(matrix[i]) if c!='.'])
    owps = sum(owp(matrix, j) for j in range(len(matrix)) if j in indices)
    return owps / len(indices)

def rpi(matrix, i):
    return wp(matrix, i) / 4 + owp(matrix, i) / 2 + oowp(matrix, i) / 4

def f(matrix):
    return [rpi(matrix, i) for i in range(len(matrix))]

T = int(raw_input())
for case in range(1, T+1):
    N = int(raw_input())
    matrix = [list(s) for s in [raw_input() for _ in range(N)]]
    res = f(matrix)
    print 'Case #{0}:'.format(case)
    print '\n'.join('{0}'.format(x) for x in res)

