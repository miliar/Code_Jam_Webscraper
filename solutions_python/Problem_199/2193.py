#!/usr/bin/env python3


def flip_first_n_pancakes(pancake_row, n, start_pos):
    assert len(pancake_row) >= n + start_pos
    new_pancake_row = []
    for index, pancake in enumerate(pancake_row):
        if start_pos <= index < n + start_pos:
            new_pancake_row.append(1 - pancake)
        else:
            new_pancake_row.append(pancake)
    return new_pancake_row


def check_all_ones(pancake_row):
    for pancake in pancake_row:
        if pancake == 0:
            return False
    return True


def make_all_ones(pancake_row, flipper_size):
    current_row = pancake_row
    counter = 0
    for i in range(len(current_row) - flipper_size + 1):
        if current_row[i] == 0:
            current_row = flip_first_n_pancakes(current_row, flipper_size, i)
            counter += 1
    return (check_all_ones(current_row), counter)


def transform(input_row):
    output_row = []
    for symbol in input_row:
        assert symbol in ["+", "-"]
        if symbol == "+":
            output_row.append(1)
        elif symbol == "-":
            output_row.append(0)
    return output_row


def parse_file(filename):
    input_data = []
    for index, line in enumerate(open(filename)):
        if index > 0:
            data = line.strip().split()
            input_data.append((transform(data[0]), int(data[1])))
    return input_data


def main(data):
    for index, datum in enumerate(data):
        result = make_all_ones(datum[0], datum[1])
        if result[0]:
            print("Case #{0}: {1}".format(index+1, result[1]))
        else:
            print("Case #{0}: IMPOSSIBLE".format(index+1))


if __name__ == "__main__":
    from sys import argv
    main(parse_file(argv[1]))
