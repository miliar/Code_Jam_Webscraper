
from __future__ import division

import sys
from collections import Counter
import itertools
from pprint import pprint
from copy import copy


def write_output(output):
    lines = []
    for i, out in enumerate(output):
        line = 'Case #{}: {} {}'.format(i + 1, out[0], out[1])
        lines.append(line)

    txt = '\n'.join(lines) + '\n'
    with open(r'C:\codejam\output.txt', 'w') as f:
        f.write(txt)


def war_choice(told, blocks):
    # Blocks list is sorted.
    # Gets the lightest block heavier than told
    for i, block in enumerate(blocks):
        if block > told:
            return blocks.pop(i)
    else:
        # Or if none of the blocks are heavier, return the lightest block.
        return blocks.pop(0)


def war(num_blocks, naomi_blocks, ken_blocks):
    # sort block weights, makes choice easier
    naomi_blocks.sort()
    ken_blocks.sort()

    # Get
    naomi_points = 0
    ken_points = 0
    while naomi_blocks:
        naomi_choice = naomi_blocks.pop()
        ken_choice = war_choice(naomi_choice, ken_blocks)
        if naomi_choice > ken_choice:
            naomi_points += 1
        else:
            ken_points += 1

    return naomi_points


def deceitful_war_told_choice(naomi_blocks, ken_blocks):
    # Blocks are already sorted

    # If naomi's lowest block is lower than kens lowest block, told value should
    # be lower than kens highest block, but higher than kens second hightest block.
    # Ken will choose highest value, naomi will choose lowest value.

    # If naomi has no blocks lower than kens lowest block, her told value
    # will always be higher than kens highest block, ken will choose his lowest
    # block, and so will naomi.

    if naomi_blocks[0] < ken_blocks[0]:
        low_val = ken_blocks[-2] if len(ken_blocks) > 1 else 0
        naomi_told = ken_blocks[-1] - ((ken_blocks[-1] - low_val) / 2)
        ken_choice = ken_blocks.pop(-1)
        naomi_choice = naomi_blocks.pop(0)

    else:
        high_val = 1.0
        naomi_told = ken_blocks[-1] + ((high_val - ken_blocks[-1]) / 2)
        ken_choice = ken_blocks.pop(0)
        naomi_choice = naomi_blocks.pop(0)

    return naomi_told, naomi_choice, ken_choice


def deceitful_war(num_blocks, naomi_blocks, ken_blocks):
    # sort block weights, makes choice easier
    naomi_blocks.sort()
    ken_blocks.sort()
    # Get
    naomi_points = 0
    ken_points = 0
    while naomi_blocks:
        naomi_told, naomi_choice, ken_choice = deceitful_war_told_choice(naomi_blocks, ken_blocks)
        if naomi_choice > ken_choice:
            naomi_points += 1
        else:
            ken_points += 1

    return naomi_points


def process(num_blocks, naomi_blocks, ken_blocks):
    war_points = war(num_blocks, copy(naomi_blocks), copy(ken_blocks))
    deceitful_war_points = deceitful_war(num_blocks, copy(naomi_blocks), copy(ken_blocks))
    return [deceitful_war_points, war_points]


def main():
    output = []

    filepath = r'C:\codejam\input.txt'
    with open(filepath, 'r') as f:
        num_cases = int(f.readline().strip())
        for i in range(num_cases):
            num_blocks = int(f.readline().strip())
            naomi_blocks = map(float, f.readline().strip().split())
            ken_blocks = map(float, f.readline().strip().split())
            output.append(process(num_blocks, naomi_blocks, ken_blocks))

    write_output(output)


if __name__ == '__main__':
    main()
