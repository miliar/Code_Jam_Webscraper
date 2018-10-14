#!/usr/bin/env python3


def find_first_untidiness(num_string):
    for i in range(len(num_string) - 1):
        if int(num_string[i]) > int(num_string[i+1]):
            return (True, i+1)
    return (False, -1)


def find_tidy_number(num_string):
    res, pos = find_first_untidiness(num_string)
    if not res:
        return num_string
    else:
        head = str(int(num_string[:pos]) - 1)
        tail = "9" * (len(num_string) - pos)
        return head + tail


def iter_tidy(num_string):
    curr_string = num_string
    while find_tidy_number(curr_string) != curr_string:
        curr_string = find_tidy_number(curr_string)
    return curr_string


def parse_input(filename):
    dataset = []
    for index, line in enumerate(open(filename)):
        if index > 0:
            dataset.append(line.strip())
    return dataset


def main(filename):
    dataset = parse_input(filename)
    for index, num_string in enumerate(dataset):
        print("Case #{0}: {1}".format(index+1, int(iter_tidy(num_string))))


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
