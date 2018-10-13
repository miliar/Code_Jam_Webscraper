#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import combinations, product

D = {"^" : (-1, 0), ">" : (0, 1), "<" : (0, -1), "v" : (1, 0)}


def f(R, C, M):
    c_r = [0 for _ in range(R)]
    c_c = [0 for _ in range(C)]
    for i in range(R):
        for j in range(C):
            if M[i][j] != ".":
                c_r[i] += 1
                c_c[j] += 1
    result = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] != ".":
                if c_r[i] == 1 and c_c[j] == 1:
                    return "IMPOSSIBLE"
                move = M[i][j]
                now = i, j
                while True:
                    now = now[0] + D[move][0], now[1] + D[move][1]
                    if now[0] < 0 or now[0] >= R or now[1] < 0 or now[1] >= C:
                        result += 1
                        break
                    if M[now[0]][now[1]] != ".":
                        break
    return result






def main():
    f_name = "A-large"
    in_f = "{0}.in".format(f_name)
    out_f = "{0}.out".format(f_name)
    with open(in_f) as in_file, open(out_f, "w") as out_file:
        input_f = lambda :next(in_file).strip()
        read_int = lambda :int(input_f())
        read_ints = lambda :map(int, input_f().split(' '))
        read_lines = lambda n:[input_f() for i in range(n)]
        T = read_int()
        for i in range(T):
            R, C = read_ints()
            M = read_lines(R)
            result = f(R, C, M)
            print "Case #{0}: {1}".format(i + 1, result)
            out_file.write("Case #{0}: {1}\n".format(i + 1, result))


if __name__ == "__main__":
    main()
