#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import product

def g(V, X, r_gt, c_gt, r_lt, c_lt):
    t_lt = (V * (c_gt - X)) / ((c_gt - c_lt) * r_lt)
    t_gt = (V * (X - c_lt)) / ((c_gt - c_lt) * r_gt)
    return max(t_lt, t_gt)

def f(N, V, X, R_C):
    l_gt = []
    l_eq = []
    l_lt = []
    for _r, _c in R_C:
        if _c > X:
            l_gt.append((_r, _c))
        elif _c == X:
            l_eq.append((_r, _c))
        else:
            l_lt.append((_r, _c))
    result = None
    if len(l_eq) != 0:
        result = V / sum(_r for _r, _ in l_eq)

    if len(l_gt) != 0 and len(l_lt) != 0:
        result = min(g(V, X, r_gt, c_gt, r_lt, c_lt) for (r_gt, c_gt), (r_lt, c_lt) in product(l_gt, l_lt))


    if result is None:
        return "IMPOSSIBLE"
    else:
        return "{0:.10f}".format(result)

def main():
    f_name = "B-small-attempt3"
    in_f = "{0}.in".format(f_name)
    out_f = "{0}.out".format(f_name)
    with open(in_f) as in_file, open(out_f, "w") as out_file:
        input_f = lambda :next(in_file).strip()
        read_int = lambda :int(input_f())
        read_ints = lambda :map(int, input_f().split(' '))
        read_floats = lambda :map(float, input_f().split(' '))
        read_lines = lambda n:[input_f() for i in range(n)]
        T = read_int()
        for i in range(T):
            N, V, X = read_floats()
            N = int(N)
            R_C = [read_floats() for _ in range(N)]
            result = f(N, V, X, R_C)
            print "Case #{0}: {1}".format(i + 1, result)
            out_file.write("Case #{0}: {1}\n".format(i + 1, result))


if __name__ == "__main__":
    main()
