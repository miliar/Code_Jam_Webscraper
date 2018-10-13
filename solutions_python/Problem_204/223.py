import math
import sys
from munkres import Munkres, make_cost_matrix


def cal_range(y, x):
    st = int(math.floor(y / 1.1 / x))
    ed = int(math.ceil(y / 0.9 / x))
    if ed * x * 0.9 > y:
        ed -= 1
    if st * x * 1.1 < y:
        st += 1
    return (0, 0) if st > ed else (st, ed)


t = input()
for cas in range(t):
    n, p = map(int, raw_input().split())
    r = map(int, raw_input().split())
    q = [map(int, raw_input().split()) for _ in xrange(n)]

    q_range = [[cal_range(q[i][j], r[i]) for j in xrange(p)] for i in xrange(n)]

    res = 0
    if n == 1:
        res = sum(ed != 0 for st, ed in q_range[0])
    else:
        matrix = []
        for i in xrange(p):
            l1, r1 = q_range[0][i]
            if r1 == 0:
                matrix.append([0] * p)
            else:
                row = []
                for j in xrange(p):
                    l2, r2 = q_range[1][j]
                    if r2 == 0:
                        row.append(0)
                    else:
                        if (((l1 <= l2 and l2 <= r1) and (l2 <= r1 and r1 <= r2))
                            or ((l2 <= l1 and l1 <= r2) and (l1 <= r2 and r2 <= r1))):
                            row.append(1)
                        else:
                            row.append(0)
                matrix.append(row)

        cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
        m = Munkres()
        indexes = m.compute(cost_matrix)
        res = sum(matrix[r][c] for r, c in indexes)

    print 'Case #{0}: {1}'.format(cas+1, res)
