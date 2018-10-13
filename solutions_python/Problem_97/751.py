# encoding: utf-8


from __future__ import division

import sys
import time


def candidates(num):
    number = str(num)
    length = len(number)
    cands = []

    for i in range(1, length):
        cand = ""
        for j in range(length):
            cand += number[(i+j)%length]
        cands.append(int(cand))

    return cands


def main(input):
    """ Recycled Short Problem

    """

    # Create empty solution output file
    with open('sol.txt', 'w') as f:
        pass

    data = file(input)
    NUM_CASES = int(data.readline())

    print "Cases:", NUM_CASES

    for case in range(NUM_CASES):

        params = data.readline()

        # Magic in here

        ranges = map(int, params.split())

        matches = {}
        count = 0

        for i in xrange(ranges[0], ranges[1]):
            cands = candidates(i)

            for c in cands:
                if c > i and c <= ranges[1]:
                    # if sorted([c, i]) not in matches:
                        # matches.append(sorted([c,i]))
                    indices = sorted([c,i])
                    matches[indices[0], indices[1]] = True

        # print count
        num_matches = len(matches)

        result = num_matches

        # Fin

        print result

        # Print results in output file
        with open('sol.txt', 'a') as f:
            f.write("Case #" + str(case + 1) + ": " + str(result))
            if not case == NUM_CASES - 1:
                f.write('\n')


if __name__ == "__main__":

    start_time = time.time()

    main( sys.argv[1] if len(sys.argv) > 1 else '' )

    print "Solved in:" , time.time() - start_time, "seconds."