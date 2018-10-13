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
    spl = line.split()
    num_stalls = int(spl[0])
    num_people = int(spl[1])

    # set up our taken stalls
    taken_stalls = [False] * num_stalls
    taken_stalls.insert(0, True)
    taken_stalls.append(True)
    len_taken_stalls = len(taken_stalls)

    min_rs_ls = None
    max_rs_ls = None

    for i in range(1, num_people + 1):
        ls_list = []
        rs_list = []
        min_ls_rs_list = []
        max_ls_rs_list = []

        for j, stall_taken in enumerate(taken_stalls):
            if stall_taken:
                # Stall is taken, append None
                ls_list.append(-1)
                rs_list.append(-1)
                min_ls_rs_list.append(-1)
                max_ls_rs_list.append(-1)
                continue

            # find the closest occupied stalls
            tmp_j_left = copy(j) - 1
            while tmp_j_left >= 0:
                if taken_stalls[tmp_j_left]:
                    ls_list.append(j - tmp_j_left - 1)
                    break
                tmp_j_left -= 1

            tmp_j_right = copy(j) + 1
            while tmp_j_right < len_taken_stalls:
                if taken_stalls[tmp_j_right]:
                    rs_list.append(tmp_j_right - j - 1)
                    break

                tmp_j_right += 1

            # Add to the min list
            min_ls_rs_list.append(min(ls_list[j], rs_list[j]))
            max_ls_rs_list.append(max(ls_list[j], rs_list[j]))

        # Now we have the list of occupied stalls.
        max_of_mins = max(min_ls_rs_list)

        # Find all the indices of the possible stalls
        possible_stalls = find_indices_containing_number(min_ls_rs_list, max_of_mins)

        # Choose a stall
        if len(possible_stalls) == 1:
            # we only have one possibility, pick it
            chosen_stall = possible_stalls[0]
        else:
            # We have more than one choice - look at the max(ls, rs) values of the possible list

            max_of_possible = {}  # map of max(ls, rs) -> stall index

            for possible_index in possible_stalls:
                max_of_possible[max_ls_rs_list[possible_index]] = possible_index

            max_of_maxes = max(max_of_possible.keys())

            possible_stalls_after_maxes = []

            for k, v in max_of_possible.items():
                if k == max_of_maxes:
                    possible_stalls_after_maxes.append(v)

            # choose the left-most of the ones left
            chosen_stall = sorted(possible_stalls_after_maxes)[0]

        # Do the choosing
        taken_stalls[chosen_stall] = True
        min_rs_ls = min_ls_rs_list[chosen_stall]
        max_rs_ls = max_ls_rs_list[chosen_stall]

    return '{} {}'.format(max_rs_ls, min_rs_ls)


def find_indices_containing_number(list_of_nums, num_to_find):
    possible_stalls = []
    try:
        lowest_index = 0
        while True:
            found_min = list_of_nums.index(num_to_find, lowest_index)
            possible_stalls.append(found_min)
            lowest_index = found_min + 1
    except ValueError:
        pass
    return possible_stalls


if __name__ == '__main__':
    main()
