#!/usr/bin/env python

import sys

stdin = sys.stdin

number_of_cases = int(stdin.readline())
for test_case in xrange(1, number_of_cases + 1):
    number_of_letters_per_key, number_of_keys, letters_in_alphabet = \
            [int(x) for x in stdin.readline().strip().split()]
    frequencies = list(enumerate((int(x)
            for x in stdin.readline().strip().split())))
    frequencies.sort(cmp=lambda kf1, kf2: -cmp(kf1[1], kf2[1]))

    key_presses = 0
    current_key = 0
    number_of_presses_for_this_key = 1
    impossible = False

    for letter, freq in frequencies:
        if current_key >= number_of_keys:
            number_of_presses_for_this_key += 1
            if number_of_presses_for_this_key > number_of_letters_per_key:
                impossible = True
                break
            current_key = 0

        key_presses += freq * number_of_presses_for_this_key
        current_key += 1

    if impossible:
        print "Case #%d: Impossible" % (test_case, )
    else:
        print "Case #%d: %d" % (test_case, key_presses)

# vim:ts=4:sw=4:expandtab
