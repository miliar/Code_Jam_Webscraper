__author__ = 'moritz'

def plus(x):
    return (1, x)

def minus(x):
    return (-1, x)

i = 'i'
j = 'j'
k = 'k'

tbl = {1: {1: plus(1), i: plus(i), j: plus(j), k: plus(k)},
       i: {1: plus(i), i: minus(1), j: plus(k), k: minus(j)},
       j: {1: plus(j), i: minus(k), j: minus(1), k: plus(i)},
       k: {1: plus(k), i: plus(j), j: minus(i), k: minus(1)}
       }

class quat(object):

    def __init__(self, unit, sgn=1):
        self.unit = unit
        self.sgn = sgn

    def mult(self, other):
        res = tbl[self.unit][other.unit]
        sgn = res[0] * self.sgn * other.sgn
        unit = res[1]
        return quat(unit, sgn)


def mult_quats(s):
    q = quat(1)
    for c in s:
        q = q.mult(quat(c))
    return q

def solver(s):
    # multiplying ijk gives -1, so we can check this first
    full_prod = mult_quats(s)
    if full_prod.unit != 1 or full_prod.sgn != -1:
        return False
    left = quat(1)
    for first_cut in range(1, len(s) - 1):
        left = left.mult(quat(s[first_cut - 1]))
        if left.unit != i or left.sgn != 1:
            continue
        # multiplying j and k gives i, so check this
        rem_prod = mult_quats(s[first_cut:])
        if rem_prod.unit != i or rem_prod.sgn != 1:
            continue
        middle = quat(1)
        for second_cut in range(first_cut + 1, len(s)):
            middle = middle.mult(quat(s[second_cut - 1]))
            if middle.unit != j or middle.sgn != 1:
                continue
            right = mult_quats(s[second_cut:])
            if right.unit == k and right.sgn == 1:
                return True
    return False



def solve_case(test_case):
    l, x = [int(s) for s in raw_input().split()]
    s = raw_input() * x
    soln = solver(s)
    print("Case #{}: {}".format(test_case + 1, "YES" if soln else "NO"))


t = input()

for test_case in range(t):
    solve_case(test_case)