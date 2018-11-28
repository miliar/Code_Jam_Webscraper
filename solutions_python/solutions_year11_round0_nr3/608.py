import sys
import itertools
from operator import itemgetter


if __name__ == "__main__":

    f = open(sys.argv[1])
    testcount = int(f.readline())

    for testindex in range(0, testcount):

        candycount = int(f.readline())
        line = f.readline()
        candies = line.strip().split()

        for idx, candy in enumerate(candies):
            candies[idx] = int(candy)

        total_xor = 0
        for candy in candies:
            total_xor ^= candy
        if total_xor:
            print "Case #%i: NO" % (testindex+1)
            continue
        total_sum = sum(candies)

        possible = False

        positions = range(0, len(candies))
        positionset = set(positions)

        best_diff = -1
        best_bag_value = -1

        for poscomb_r in range(1, len(candies)/2+1):

            poscombs = itertools.combinations(positions, poscomb_r)

            for poscomb in poscombs:

                bag1_xor_value = 0
                bag2_xor_value = 0
                bag1_value = 0
                bag2_value = 0                

                for pos in poscomb:
                    bag1_xor_value ^= candies[pos]
                    bag1_value += candies[pos]

                bag2pos = positionset-set(poscomb)
                for pos in bag2pos:
                    bag2_xor_value ^= candies[pos]
                    bag2_value += candies[pos]

                if bag1_xor_value != bag2_xor_value:
                    continue

                possible = True
                diff = abs(bag1_value-bag2_value)
                if diff > best_diff:
                    best_diff = diff
                    best_bag_value = max(bag1_value, bag2_value)

        if not possible:
            print "Case #%i: NO" % (testindex+1)
        else:
            print "Case #%i: %i" % (testindex+1, best_bag_value)
