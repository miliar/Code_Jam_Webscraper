# -*- coding: utf-8 -*-

import sys
import utools.files


def is_tidy(s):
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))


def previous_tidy_number(s):
    if is_tidy(s):
        return s
    if is_tidy(s[::-1]):
        return str(int(s[0]) - 1) + previous_tidy_number("9" * (len(s) - 1))
    res = s[0] + previous_tidy_number(s[1:])
    if not is_tidy(res):
        return str(int(s[0]) - 1) + previous_tidy_number("9" * (len(s) - 1))
    return res


def process(n):
    return int(previous_tidy_number(str(n)))


def main(path):

    with open(path) as f:
        t = utools.files.read_item(f, int)
        for i in range(1, t+1):
            n = utools.files.read_item(f, int)
            result = process(n)
            print("Case #{}: {}".format(i, result))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        main(sys.argv[1])
