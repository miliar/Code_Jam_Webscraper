"""
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

"""
"""
Tidy is when digits are in non-decreasing order
"""

import sys

def tidy(number):
    """
    return the last tidy number less the the number given
    :param number: int
    :return: the last tidy number

    >>> tidy(132)
    129
    >>> tidy(1000)
    999
    >>> tidy(7)
    7
    >>> tidy(111111111111111110)
    99999999999999999
    """
    number_str = str(number)

    # check for each digit starting from the right whether it's less than the digit after it
    while True:
        if (is_tidy(number_str)):
            return int(number_str)

        for i in range(len(number_str) - 1, 0, -1):
            if int(number_str[i]) < int(number_str[i - 1]):
                # from my index to len() (last index)
                n_to_sub = int(number_str[i: len(number_str)]) + 1
                number_str = str(int(number_str) - n_to_sub)
                break

def is_tidy(number_str):
    for index in range(len(number_str) - 1):
        if int(number_str[index]) > int(number_str[index + 1]):
            return False
    return True


def main(file_name):
    f = open(file_name)

    first = True
    for index, line in enumerate(f):
        if first:
            first = False
        else:
            print("Case #{}: {}".format(index,
                                        tidy(int(line))))

    f.close()

if __name__ == '__main__':
    import math
    file_name = sys.argv[1]
    main(file_name)
    # print(1 * int(math.pow(10, 18)))