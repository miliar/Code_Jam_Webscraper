"""Tidy Number

    Thanks, Tatiana."""
from typing import List


def is_tidy(number):
    last_compared = 0
    split_list = [int(i) for i in str(number)]
    for value in split_list:
        if int(value) >= last_compared:
            last_compared = value
            continue
        else:
            return False
    return True


def get_last_tidy(numbers: List[int]):
    last_tidy = 0
    for i in numbers:
        for j in range(0, i + 1):
            if is_tidy(j):
                last_tidy = j
    return last_tidy


def test_tidiness():
    import random
    for number in random.sample(range(0, 1000), 100):
        print(number, 'is', ('tidy' if is_tidy(number) else 'not tidy'))


def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = [int(s) for s in input().split(" ")]  # read a list of integers
        print("Case #{}: {}".format(i, get_last_tidy(n)))
        # check out .format's specification for more formatting options


if __name__ == '__main__':
    main()
