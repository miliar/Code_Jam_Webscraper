# -*- coding: utf-8 -*-

from copy import copy

import click


@click.command()
@click.argument('input_file', type=click.File())
@click.argument('output_file', type=click.File(mode='w'))
def main(input_file, output_file):
    # Read in the number of cases first
    num_cases = int(input_file.readline())

    for i in range(1, num_cases + 1):
        # Solve the case
        result = solve(input_file.readline())
        # Print the output
        click.echo('Case #{}: {}'.format(i, result), file=output_file)


def solve(line):
    num = int(line)

    while num > 0:
        tmp_num = copy(num)

        highest = 9
        multiplier = 1

        while tmp_num != 0:
            last_digit = tmp_num % 10

            if last_digit > highest:
                num = tmp_num * multiplier
                break

            # update
            highest = last_digit
            tmp_num //= 10
            multiplier *= 10

        if tmp_num == 0:
            return num

        num -= 1

    return 1

if __name__ == '__main__':
    main()
