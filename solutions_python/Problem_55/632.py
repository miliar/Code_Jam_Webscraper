#!/usr/bin/env python
# Adlan Razalan <adlanism@gmail.com>
from sys import exit
from collections import deque

def solve(input_file, output_file):
    input = open(input_file, 'r')
    output = open(output_file, 'w')

    case = int(input.readline().strip())

    for i in xrange(1, case+1):
        options = input.readline().strip().split(' ', 3)
        R = int(options[0])     # round trip
        k = int(options[1])     # capacity
        N = int(options[2])     # number of groups

        group_size = [int(x) for x in input.readline().strip().split(' ', N)]

        queue = deque(group_size, N)
        total = 0

        for p in xrange(1, R+1):
            passenger = 0
            group = 0

            while passenger < k:
                if (passenger + queue[0]) > k:
                    break
                else:
                    passenger += queue[0]
                    groupn = queue.popleft()
                    group += 1

                    # this means that there is only 1 group and the
                    # roller coaster can hold enough people for that group
                    if len(queue) == 0:
                        queue.append(groupn)
                        break

                    # if the roller coaster able to handle all the group
                    if group == N:
                        queue.append(groupn)
                        group = 0
                        break

                    queue.append(groupn)

            total += 1 * passenger

        output.write("Case #%i: %i\n" % (i, total))
        i += 1

    input.close()
    output.close()

if __name__ == '__main__':
    exit(solve('C-small-attempt1.in', 'C-small-attempt1.out') or 0)
