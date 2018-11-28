#!/usr/bin/env python3

# This code jam solution is powered by Nathan West's LibCodeJam; see
# https://github.com/Lucretiel/LibCodeJam for source code and (ostensibly) some
# documentation.

from code_jam import *


# Uncomment if you want a newline between the "Case #" and the actual solution
#code_jam.INSERT_NEWLINE = True

# Example:
#
#    Case #1: solution
#    Case #2: solution
#
# vs
#
#    Case #1:
#    solution
#    Case #2:
#    solution
#

@autosolve
@collects
def solve(Smax: int, digits: str):
    audience_members = [int(i) for i in digits]

    num_needed = 0
    num_standing = 0

    for shyness, num_people in enumerate(audience_members):
        if shyness > num_standing and num_people > 0:
            extras = shyness - num_standing
            num_needed += extras
            num_standing += extras
        num_standing += num_people

    return num_needed
