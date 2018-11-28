# -*- coding: utf-8 -*-
import sys

def find_first_untidy_digit(digit_sequence):
    for i in range(len(digit_sequence)-1):
        a, b = digit_sequence[i:i+2]
        if a > b:
            return i
    return -1

def tidy_up(digit_sequence, index):
    # keep first part of list
    result = digit_sequence[0:index]
    # decrease first untidy occurence
    result += [str(int(digit_sequence[index]) - 1)]
    # fill up with 9
    result += ["9"] * (len(digit_sequence)-index-1)
    return result

def solve(question):
    digit_sequence = [c for c in question]
    while True: 
        first_untidy = find_first_untidy_digit(digit_sequence)
        if first_untidy < 0:
            break
        digit_sequence = tidy_up(digit_sequence, first_untidy)
    # cast to int, so strip possible leading zeros
    return int("".join(digit_sequence))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f_in, \
             open(sys.argv[1] + ".out", "w") as f_out:
        count = int(f_in.readline())
        for i in range(count):
            question = f_in.readline().strip()
            solution = solve(question)
            f_out.write("Case #%i: %s\n" % (i+1, str(solution)))
