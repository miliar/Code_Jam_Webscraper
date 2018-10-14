class QN:
    def __init__(self):
        self.sign = 1
        self.ijk = 0

MT_SIGN = map(int, '1 1 1 1 1 -1 1 -1 1 -1 -1 1 1 1 -1 -1'.split())
MT = map(int, '0 1 2 3 1 0 3 2 2 3 0 1 3 2 1 0'.split())
def mul(a, b):
    ret = QN()
    ret.sign = a.sign * b.sign * MT_SIGN[4 * a.ijk + b.ijk]
    ret.ijk = MT[4 * a.ijk + b.ijk]
    return ret

def is_reducible_neg_1(lst, x):
    res = QN()
    for e in lst:
        res = mul(res, e)
    if res.ijk > 0:
        if res.sign > 0:
            return x % 4 == 2
        else:
            return (x % 2 == 1 and x % 4 == 0) or (x % 2 == 0 and x % 4 == 2)
    if res.sign < 0:
        return x % 2 == 1
    return False

def rem_hw_i(lst, x):
    res = QN()
    for j in xrange(x):
        for i in xrange(len(lst)):
            res = mul(res, lst[i])
            if res.ijk == 1:
                return len(lst) * x - i - 1
    return -1

def has_jk(s):
    return 'j' in s or 'k' in s

def f(s):
    ret = QN()
    if s == 'i':
        ret.ijk = 1
    elif s == 'j':
        ret.ijk = 2
    elif s == 'k':
        ret.ijk = 3
    return ret

def chk(l, x, s):
    lst = [f(e) for e in s]
    return is_reducible_neg_1(lst, x) and rem_hw_i(lst, x) >= 2 and has_jk(s)

def main():
    t = int(raw_input())
    for k in xrange(1, t+1):
        l, x = map(int, raw_input().split())
        s = raw_input()
        print 'Case #%d: %s' % (k, 'YES' if chk(l, x, s) else 'NO')

if __name__ == '__main__':
    main()
