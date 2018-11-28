#!/usr/bin/env python2

import sys

def get_additional_people(S):
    """
    Get the number of additional people required
    :param S: string of shyness values
    :return:
    """

    audience_size = 0
    extra_required = 0

    for shyness, c in enumerate(S):
        num = int(c)

        if num > 0 and shyness > audience_size:
            extras = (shyness - audience_size)
            extra_required += extras
            audience_size += extra_required

        audience_size += num

    return extra_required

input_data = sys.stdin.readlines()

T = int(input_data[0])

for index, line in enumerate(input_data[1:]):

    S_max, S = line.strip().split()
    extras = get_additional_people(S)
    print "Case #%d: %d" % (index+1, extras)


