# -*- coding: utf-8 -*-

import sys
import utools.files

sys.setrecursionlimit(10000)


class Impossible(Exception):
    pass


def process(s, k):
    if "-" not in s:
        return 0
    if k > len(s):
        raise Impossible
    if s[0] == "+":
        return process(s[1:], k)
    for i in range(k):
        if s[i] == "+":
            s[i] = "-"
        else:
            s[i] = "+"
    return 1 + process(s[1:], k)


def main(path):

    with open(path) as f:
        t = utools.files.read_item(f, int)
        for i in range(1, t+1):
            r = utools.files.read_mutiple_items(f, list, str)
            try:
                result = process(list(r[0]), int(r[1]))
            except Impossible:
                result = "IMPOSSIBLE"
            print("Case #{}: {}".format(i, result))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        main(sys.argv[1])
