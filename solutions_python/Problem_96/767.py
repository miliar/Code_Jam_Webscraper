# encoding: utf-8


from __future__ import division

import sys
import time


def main(input):
    """ Googlers Problem

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

        numbers = map(int, params.split())

        num_googlers = numbers.pop(0)
        max_surprises = numbers.pop(0)
        p = numbers.pop(0)

        triples = []
        num_surprises = 0

        numbers.sort()
        numbers.reverse()

        for n in numbers:
            triple = []
            center = n // 3
            rest = n % 3

            triple.append(center)

            if rest == 0:
                if num_surprises < max_surprises and center != 0 and center < p:
                    triple.append(center + 1)
                    triple.append(center - 1)
                    num_surprises += 1
                else:
                    triple.append(center)
                    triple.append(center)
            elif rest == 1:
                triple.append(center)
                triple.append(center + 1)
            else:
                if num_surprises < max_surprises and center != 0 and center < p:
                    triple.append(center)
                    triple.append(center + 2)
                    num_surprises += 1
                else:
                    triple.append(center + 1)
                    triple.append(center + 1)

            triples.append(triple)

        maxes = [max(t) for t in triples]

        mayores = sum(m >= p for m in maxes)

        result = mayores

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