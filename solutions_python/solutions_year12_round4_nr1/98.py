#!/usr/bin/env python
#-*- coding:utf-8 -*-



def f(D, ls):
    d_l = dict(ls)
    d_from_list = dict((d, []) for d in d_l.keys())
    d_l[0] = [0]
    d_from_list[ls[0][0]] = [0]
    print d_from_list
    for d, l in ls:
        for d_from in d_from_list[d]:
            d_to = can_to(d_from,d_l[d_from], d, l)
            if d_to >= D:
                return "YES"
            for _d, _ in ls:
                if d < _d <= d_to:
                    if d not in d_from_list[_d]:
                        d_from_list[_d].append(d)
    return "NO"


def can_to(now_d, now_l, to_d, to_l):
    return min(to_d - now_d, to_l) + to_d


def main():
    in_f = "A-small-attempt1.in"
    out_f = "A.out"
    with open(in_f) as in_file, open(out_f, "w") as out_file:
        input_f = lambda :next(in_file)
        read_int = lambda :int(input_f())
        read_ints = lambda :map(int, input_f().split(' '))
        read_lines = lambda n:[input_f().strip() for i in range(n)]
        T = read_int()
        for i in range(T):
            n = read_int()
            ls = [read_ints() for j in range(n)]
            d = read_int()
            result = f(d, ls)
            print "Case #{0}: {1}".format(i + 1, result)
            out_file.write("Case #{0}: {1}\n".format(i + 1, result))


if __name__ == "__main__":
    main()
