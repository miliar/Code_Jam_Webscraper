#!/usr/bin/python

import itertools
import sys
import time

DEBUG = False


def main():
    T = int(sys.stdin.readline())
    for i in range(1, T + 1):
        test_data = read_test_data()

        if DEBUG:
            start_time = time.time()
            print "Case #{} INPUT: {}".format(i, test_data)
            print "Case #{}: {}".format(i, compute_test_result(test_data))
            elapsed = time.time() - start_time
            print "TIME: {:.2f}s".format(elapsed)
            print
        else:
            print "Case #{}: {}".format(i, compute_test_result(test_data))


def readline(types):
    objects = []
    type_index = 0

    for token in sys.stdin.readline().split():
        objects.append(types[type_index](token))

        if type_index + 1 < len(types):
            type_index += 1

    return objects


def split_list(raw_list, index):
    return raw_list[:index] + [raw_list[index:]]


def read_test_data():
    all = readline([int])
    return all[0], all[1:]


# R O Y G B V
# basic colors: R Y B
# O surrounded by B
# G surrounded by R
# V surrounded by Y

def color_map(index):
    return ["R", "O", "Y", "G", "B", "V"][index]

def substitutions(colors):
    substs = [0 for _ in range(6)]
    for i in range(6):
        if (i % 2):
            val = colors[i]
            substs[i] = val
            colors[i] -= val
            colors[(i+3)%6] -= val

    return substs

def get_compatible(colors, color):
    for i in range(len(colors)):
        if i != color and colors[i]:
            colors[i] -= 1
            return i
    return None

def verify(colors):
    for i in range(len(colors)):
        if colors[i] == colors[(i+1)%len(colors)]:
            assert False

def compute_test_result(test_data):
    N, colors = test_data
    assert N == sum(colors)

    substs = substitutions(colors)

    for i in range(6):
        if substs[i] and colors[(i+3)%6] == 0:
            if 2 * substs[i] == N:
                numbers = [i, (i+3)% 6] * substs[i]
                output = "".join(list(map(color_map, numbers)))
                return output
            else:
                return "IMPOSSIBLE"

    # any color appear more than half?
    for color in colors:
        if color * 2 > sum(colors):
            return "IMPOSSIBLE"

    dom_value = max(colors)
    dom_index = colors.index(dom_value)

    # take out
    colors[dom_index] = 0

    buckets = [[] for _ in range(dom_value)]

    for i in range(dom_value):
        buckets[i].append(dom_index)
        swap_index = (dom_index+3)%6
        while substs[swap_index]:
            buckets[i].append(swap_index)
            buckets[i].append(dom_index)
            substs[swap_index] -= 1
        # color = max(colors)
        # color_index = colors.index(color)
        # colors[color_index] -= 1
        #
        # buckets[i].append(color_index)


    output = "".join(list(map(color_map, itertools.chain(*buckets))))
    assert len(output) + sum(colors) + 2*sum(substs) == N

    while(len(output) + 2*sum(substs) < N):
        for i in range(dom_value):
            color = get_compatible(colors, buckets[i][-1])
            if color is not None:
                buckets[i].append(color)

                swap_index = (color+3)%6
                while substs[swap_index]:
                    buckets[i].append(swap_index)
                    buckets[i].append(color)
                    substs[swap_index] -= 1

        output = "".join(list(map(color_map, itertools.chain(*buckets))))
        assert len(output) + sum(colors) + 2*sum(substs) == N

        #print output
        #print colors
    # print "{} {}".format(len(output), N)
    # print output
    # print substs
    assert len(output) == N
    verify(output)
    return output

if __name__ == "__main__":
    main()
