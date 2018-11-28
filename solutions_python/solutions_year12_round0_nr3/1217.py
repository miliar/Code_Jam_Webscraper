#!/usr/bin/python2.6

# Standard libs
import collections
import sys

def get_number_of_recycled_pairs(lower_bound, upper_bound):
    # Invalid bounds
    if lower_bound >= upper_bound:
        return 0

    # Bounds have different number of digits
    if len(str(lower_bound)) != len(str(upper_bound)):
        return 0

    pairs = set()

    for n in range(lower_bound, upper_bound + 1):
        digits = list(str(n))
        rotated_digits = collections.deque(digits)

        # Rotate each number in the range
        for i in range(len(digits) - 1):
            rotated_digits.rotate(1)
            rotated_n = int("".join(list(rotated_digits)))

            # If the rotated number is also in the range,
            # add it as a tuple to the set of pairs
            if n != rotated_n and rotated_n >= lower_bound and rotated_n <= upper_bound:
                # Create a tuple so that the smaller number is first.
                # (Just a convention to guarantee uniqueness)
                if n < rotated_n:
                    pairs.add((n, rotated_n))
                else:
                    pairs.add((rotated_n, n))

    return len(pairs)

def process_line(input_line):
    split_line  = [int(i) for i in input_line.split()]
    lower_bound = split_line[0]
    upper_bound = split_line[1]
    return str(get_number_of_recycled_pairs(lower_bound, upper_bound))

def main(argv):
    if len(argv) != 2:
        print "Usage: python %s INPUT_FILE" % (sys.argv[0])
        return 1

    input_filepath = argv[1]

    with open(input_filepath, "r") as input_file:
        print "\n".join([
            "Case #%d: %s" % (i + 1, process_line(line.strip()))
            for i, line
            in enumerate(input_file.readlines()[1:])
        ])

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

