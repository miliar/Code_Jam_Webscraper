#!/usr/bin/python
"""
Tidy Numbers
"""
import sys, os


def solve(a):
    """Returns a string result to one case of a problem"""
    if int(a) < 10:
        return a
    return tidy(a)


def tidy_sylable(data):
    if (len(data) > 2):
        print ("Syllable {} has invalid length {}!".format(data, len(data)))
        assert False
    if is_tidy(data):
        return data, False
    if (len(data) < 2):
        return data, False
    if (data == "00"):
        return "99", True
    if (data[1] == "0"):
        return str(int(data[0])-1) + "9", True
    new_data = str(int(data) - 1).zfill(2)
    return tidy_sylable(new_data)


def is_tidy(data):
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def tidy(data):
    i = 0
    while (i < len(data)-1):
        prefix = data[:i]
        syllable = data[i:i + 2]
        suffix = data[i + 2:]
        (tidy_syllable, reset) = tidy_sylable(syllable)
        suffix_new = suffix if not reset else "9"*len(suffix)
        # print(
        #     "{}:\t{}\033[91m{}\033[0m{} \t{}\033[94m{}\033[0m{} {}"
        #         .format(
        #         i,
        #         prefix,
        #         syllable,
        #         suffix,
        #         prefix,
        #         tidy_syllable,
        #         suffix_new,
        #         "RST" if reset else ""
        #     )
        # )
        i = i + 1
        data = prefix + tidy_syllable + suffix_new
        if reset:
            break
    return str(int(data)) if is_tidy(data) else tidy(data)

# Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        cases = int(f_in.readline().strip())
        for case in range(1, cases + 1):
            # Get input data
            # a = [int(x) for x in f_in.readline().strip().split()]
            a = f_in.readline().strip()
            # Solve and output
            print("Case #{}: {}".format(case, solve(a)))


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '" + str(sys.argv[1]) + "' does not exist!"
    else:
        print "No file supplied! Run program this way: '" + str(
            sys.argv[0]) + " something.in'"
