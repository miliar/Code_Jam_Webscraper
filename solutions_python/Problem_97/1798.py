import itertools
import sys

def get_combinations(iter, k):

    def _get_sub_comb(idx, j):
        res = []
        if j >= k:
            return [[i] for i in iter[idx:]]
        for i in xrange(idx, len(iter)):
            res.extend([([iter[i]] + (sc if isinstance(sc, list) else [sc])) for sc in _get_sub_comb(i, j + 1)])
        return res

    return _get_sub_comb(0, 1)

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_comb_perms(comb):

    res = [comb[0]]
    x = {}
    for i in digits:
        x[i] = 0
    for i in comb[1:]:
        x[i] += 1

    k = len(comb) - 1
    def get_perms(j):
        if j == k:
            return []
        res = []
        for i, xval in enumerate(x):
            i_ = str(i)
            if x[i_] > 0:
                x[i_] -= 1
                perms = get_perms(j + 1)
                if perms:
                    res.extend([[i_] + (r if isinstance(r, list) else [r]) for r in perms])
                else:
                    res.extend([[i_]])
                x[i_] += 1
        return res

    return [res + r for r in get_perms(0)]


def get_fit_num(comb, a, b):
    x = int(''.join(comb))
    return x >= a and x <= b


def solve(a, b):
    k = len(a)

    a = int(a)
    b = int(b)

    s = 0

    _ds = set()
    for c in get_combinations(digits, k):
        for p in get_comb_perms(c):
            p_ = [i for i in p]
            rec_num = 0
            if get_fit_num(p, a, b):
                rec_num += 1
            ds = set()
            # ds = set([int(''.join(p))])
            _ds.add(int(''.join(p)))
            for i in xrange(len(p) - 1):
                p_.insert(0, p_.pop())
                if p_[0] == 0:
                    continue
                if get_fit_num(p_, a, b):
                    p_int = int(''.join(p_))
                    if not p_int in ds and not p_int in _ds:
                        rec_num += 1
                        # ds.add(p_int)
                        _ds.add(p_int)
                    elif p_int in _ds:
                        break
            if rec_num > 1:
                s += rec_num * (rec_num - 1) / 2

    return s

def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            
            res = solve(*input_f.readline().strip().split(' '))
            output_f.write("Case #%d: %s\n" % (test_case_i + 1, res))
            
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
