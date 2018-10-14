# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import numpy as np

def solution(places, persons):
    #return something
    #step 1: determine the layer, l + 1
    used_layer = int(np.log2(persons ))   # persons + 1??
    used_places = 2 ** (used_layer) - 1
    left_places = places - used_places
    left_persons = persons - used_places
    #print left_places, left_persons, used_layer

    #step 2: determine which part of places belong to
    choice_min = left_places/(2 **(used_layer))
    num_choice_max = left_places - 2 ** (used_layer) * choice_min
    num_choice_min = 2 ** (used_layer) - num_choice_max
    #print choice_min, num_choice_max, num_choice_min
    if left_persons <= num_choice_max:
        choice = choice_min + 1
    else:
        choice = choice_min

    #step 3: determine max and min according to the odd/even
    if choice % 2 == 0:
        r_max = choice /2
        r_min = r_max - 1
    else:
        r_max = r_min = choice/2

    return r_max, r_min

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #do Solution:
    #
    #result = solution()
    r_max, r_min = solution(N, K)

    print "Case #{0}: {1} {2}".format(i, r_max, r_min)
    # check out .format's specification for more formatting options