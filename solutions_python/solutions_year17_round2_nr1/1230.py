# -*- coding: utf-8 -*-

import sys
import utools.files

compatibility = {"R": "BYG", "B": "RYO", "Y": "RBV", "O": "B", "G": "R", "V": "Y"}

sys.setrecursionlimit(10000)


def process(d, kis, sis):

    max_delay = max((d - ki) / si for ki, si in zip(kis, sis))
    return d / max_delay
        


def main(path):

    with open(path) as f:
        t = utools.files.read_item(f, int)
        for i in range(1, t+1):
            d, n = utools.files.read_mutiple_items(f, tuple, int)
            kis, sis = [], []
            for _ in range(n):
                ki, si = utools.files.read_mutiple_items(f, tuple, int)
                kis.append(ki)
                sis.append(si)

            res = process(d, kis, sis)
            print("Case #{}: {}".format(i, res))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        main(sys.argv[1])
