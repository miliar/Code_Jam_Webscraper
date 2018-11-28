#!/usr/bin/python3

import sys


def main():
    with open(sys.argv[1]) as input_file:
        content = [line.strip('\n') for line in input_file.readlines()]

    case_count = int(content[0])

    with open('output', 'w') as output_file:
        for case_number in range(1, case_count + 1):
            case_input = content[case_number]

            # Do computations here
            result = fill_stalls(case_input)

            output_file.write('Case #' + str(case_number) + ": " + str(max(result)) + ' ' +  str(min(result)) + '\n')


def fill_stalls(case_input):
    n = int(case_input.split(' ')[0])
    k = int(case_input.split(' ')[1])

    gaps = Node(n)

    for i in range(k - 1):
        gap = gaps.val

        if gap == 1:
            return 0, 0

        if gap % 2 == 0:
            lgap = int(gap / 2 - 1)
            rgap = int(gap / 2)
        else:
            lgap = rgap = int(gap / 2)

        if lgap > 0:
            sort_insert(gaps, lgap)
        if rgap > 0:
            sort_insert(gaps, rgap)
        gaps = gaps.next

    if gaps.val % 2 == 0:
        return int(gaps.val / 2 - 1), int(gaps.val / 2)
    else:
        return int(gaps.val / 2), int(gaps.val / 2)


def sort_insert(nodes, val):
    if val > nodes.val:
        return Node(val, nodes)

    start = nodes
    inserted = False

    while nodes.next is not None and not inserted:
        if val > nodes.next.val:
            nodes.next = Node(val, nodes.next)
            inserted = True
        nodes = nodes.next

    if not inserted:
        nodes.next = Node(val)

    return start


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


if __name__ == '__main__':
    main()
