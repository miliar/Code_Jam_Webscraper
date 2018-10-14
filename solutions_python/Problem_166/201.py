#!/usr/bin/env python3
import itertools
import sys


def main():
    input_file = sys.argv[1]
    solve(input_file)


def solve(input_file):
    with open(input_file) as f_in:
        t = int(next(f_in))
        for case in range(t):
            k, l, s = tuple(int(num) for num in next(f_in).split())
            keyboard = next(f_in).rstrip()
            target = next(f_in).rstrip()
            output = solve_instance(keyboard, target, s)
            print("Case #%d: %.7f" % (case + 1, output))


def solve_instance(keyboard, target, s):
    occurences = []
    for result in itertools.product(keyboard, repeat=s):
        occurences.append(count_occurrences(target, "".join(result)))
    mean_occurences = float(sum(occurences)) / len(occurences)
    return max(occurences) - mean_occurences


def count_occurrences(target, text):
    lt = len(target)
    count = 0
    idx = 0
    while True:
        idx = text.find(target, idx)
        if idx == -1:
            return count
        else:
            count += 1
            idx += 1
        

if __name__ == '__main__':
    main()
