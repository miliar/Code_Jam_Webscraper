import sys
import itertools
import collections

def validate_combo(combo):
    # if they are equal to start with skip
    if combo[0] == combo[1]:
        return False

    num_one = collections.deque(str(combo[0]))
    num_two = str(combo[1])

    # test if num_one can be
    # reorderd to num_two
    for i in range(1, len(num_one)):
        num_one.rotate(1)

        if "".join(num_one) == num_two:
            return True

    return False

def main():
    file_name = sys.argv[1]
    input_file = open(file_name, "r").readlines()
    test_cases = int(input_file[0])

    for i in range(1, test_cases + 1):
        test_numbers = input_file[i].strip().split(" ")
        num_one = int(test_numbers[0])
        num_two = int(test_numbers[1])

        num_list = [j for j in range(num_one, num_two + 1)]
        combos = itertools.product(num_list, num_list)
        combos = [j for j in combos if j[1] >= j[0]]

        num_pass = 0
        for combo in combos:
            if validate_combo(combo):
                num_pass += 1

        print "Case #%s: %s" % (i, num_pass)

if __name__ == "__main__":
    main()
