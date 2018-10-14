# encoding: utf-8


from __future__ import division

import sys
import time


def main(input):
    """ Googlerese Problem.

    """

    # Create empty solution output file
    with open('sol.txt', 'w') as f:
        pass

    data = file(input)
    NUM_CASES = int(data.readline())

    print "Cases:", NUM_CASES

    goog = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

    eng = ["our language is impossible to understand",
            "there are twenty six factorial possibilities",
            "so it is okay if you want to just give up"]

    gletters = ""
    eletters = ""

    mappings = {}

    for line in eng:
        eletters += line

    for line in goog:
        gletters += line

    for i, l in enumerate(gletters):
        if l not in mappings:
            mappings[l] = eletters[i]

    mappings['z'] = 'q'
    mappings['q'] = 'z'

    for case in range(NUM_CASES):

        params = data.readline()
        word = params.strip()

        # Magic in here

        trans = ""

        for l in word:
            trans += mappings[l]

        result = trans

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