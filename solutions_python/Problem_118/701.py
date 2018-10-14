import math
import bisect

max_len = 52  # safe


def generate_roots(max_len):
    def add1(a, i, b1, b2):
        for b in (b1, b2):
            for c in b:
                for d in c:
                    a[i] = int(d)
                    i += 1
        return i
    def add2(a, i, x):
        a[i] = int(x)
        i += 1
        return i
    add3 = add2
    # Precondition: max_len >= 2
    r = [None for i in range(50000)]
    n = 0
    odd0 = [["1"],[],[],[],[],[],[],[],[]]
    even0 = [[],["11"],[],[],[],[],[],[],[]]
    n = add1(r, n, odd0, even0)
    n = add2(r, n, "2")
    n = add2(r, n, "22")
    n = add3(r, n, "3")
    k = 2
    while k < max_len:
        ### 1
        khalf = k // 2
        odd1 = [[] for i in range(9)]
        even1 = [[] for i in range(9)]
        for i in (1, 3, 5, 7):
            for x in even0[i]:
                assert k == len(x)
                x_ = x[:khalf]
                _x = x[khalf:]
                odd1[i].append(x_ + "0" + _x)
                odd1[i + 1].append(x_ + "1" + _x)
                even1[i].append(x_ + "00" + _x)
                if i != 7:
                    even1[i + 2].append(x_ + "11" + _x)
        #
        n = add1(r, n, odd1, even1)
        even0 = even1

        ### 2
        khalfm1 = khalf - 1
        n = add2(r, n, "1" + "0" * khalfm1 + "2" + khalfm1 * "0" + "1")
        n = add2(r, n, "2" + (k - 1) * "0" + "2")
        n = add2(r, n, "2" + "0" * khalfm1 + "1" + khalfm1 * "0" + "2")
        n = add2(r, n, "2" + k * "0" + "2")
        khalfm2 = khalf - 2
        for i in range(khalfm1):
            j = khalfm2 - i
            n = add2(r, n, "1" + i * "0" + "1" + j * "0" + "2" + \
                     "0" * j + "1" + "0" * i + "1")

        k += 2
    r = r[:n]
    r.sort()
    return r


r = generate_roots(max_len)


def count(lo, hi):
    lodex = bisect.bisect_left(r, lo)
    hidex = bisect.bisect_right(r, hi)
    assert hidex < len(r) - 2  # safe
    return hidex - lodex


def case(file):
    [a, b] = [int(x) for x in file.readline().strip().split()]
    return str(count(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b))))



def cases(in_name, func=None, out_name=None):
    if func is None:
        func = case
    if out_name is None:
        ext = in_name.rindex('.')
        out_name = in_name[:ext] + ".out"
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            ntests = int(fin.readline())
            for i in range(1, ntests + 1):
                fout.write("Case #%i: %s\n" % (i, func(fin)))

cases("C-large-1.in")





def testing():
    max_len = 22
    a = []
    with open("fair_squares.txt", 'r') as fin:
        for line in fin:
            line = line.strip()
            if len(line) <= max_len:
                a.append(int(line))
    r0 = generate_roots(max_len)
    assert a == r0
    assert a == r[:1420]
    return len(a)
