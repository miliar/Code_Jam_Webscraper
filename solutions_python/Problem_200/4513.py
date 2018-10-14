import sys

def is_tidy(num):
    digits = list(str(num))
    sorted_digits = sorted(digits)

    return sorted_digits == digits


def find_highest_tidy(max_num):
    for num in reversed(range(max_num + 1)):
        if is_tidy(num):
            break

    return num


def main(input_path):

    input_file = open(input_path, 'rb')
    tests_amount = int(input_file.readline())
    tests = input_file.readlines()

    for i in range(tests_amount):
        print 'Case #{}: {}'.format(i + 1, find_highest_tidy(int(tests[i])))


if __name__ == "__main__":
    main(sys.argv[1])
