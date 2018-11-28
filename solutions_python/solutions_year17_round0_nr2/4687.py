#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
import sys


def is_increasing_no(n):
    return sorted(str(n)) == list(str(n))


def largest_tidy_no(N):
    for n in reversed(range(1, N + 1)):
        if is_increasing_no(n):
            return n


def main():
    print("here")
    filename = sys.argv[1]
    with open(filename, "r") as f:
        with open(filename.replace(".in", ".out"), "w") as f2:
            for i, line in enumerate(f.readlines()):
                if i != 0:
                    f2.write("Case #{}: {}\n".format(i, largest_tidy_no(int(line.strip()))))

            print(i, int(line.strip()))

if __name__ == "__main__":
    main()
