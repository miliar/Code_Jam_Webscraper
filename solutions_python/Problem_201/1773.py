# -*- coding: utf-8 -*-

import sys
import utools.files


def find_stale(stales):
    res = {}
    for i, v in enumerate(stales):
        if v:
            continue
        ls = 0
        j = i - 1
        while j >= 0 and not stales[j]:
            ls += 1
            j -= 1
        rs = 0
        j = i + 1
        while j < len(stales) and not stales[j]:
            rs += 1
            j += 1

        res[i] = (min(ls, rs), max(ls, rs), i)
    s = min(res, key=lambda i: (-res[i][0], -res[i][1], i))
    return s, res[s][0], res[s][1]


def process(n, k):
    stales = [True]
    for i in range(n):
        stales.append(False)
    stales += [True]

    for i in range(k):
        s, minlr, maxlr = find_stale(stales)
        stales[s] = True

    return minlr, maxlr


def main(path):

    with open(path) as f:
        t = utools.files.read_item(f, int)
        for i in range(1, t+1):
            n, k = utools.files.read_mutiple_items(f, tuple, int)
            minlr, maxlr = process(n, k)
            print("Case #{}: {} {}".format(i, maxlr, minlr))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        main(sys.argv[1])
