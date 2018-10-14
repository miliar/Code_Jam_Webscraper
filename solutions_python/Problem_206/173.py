#!/usr/bin/python

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
    dest, horse_count = readline([int, int])
    horses = []
    for _ in range(horse_count):
        horses.append(readline([int, int]))

    return dest, horses

def compute_test_result(test_data):
    dest, horses = test_data

    def speed(horse):
        time = float(dest - horse[0])/horse[1]
        return float(dest)/time

    max_speed = speed(horses[0])
    for horse in horses:
        max_speed = min(max_speed, speed(horse))

    return max_speed

if __name__ == "__main__":
    main()
