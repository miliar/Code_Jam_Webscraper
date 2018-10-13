import sys

from collections import defaultdict

def find_recycled_pairs(A, B):
    num_pairs = 0
    n_digits = len(str(A))
    for i in range(A, B+1):
        str_i = str(i)
        pair_set = set()
        for k in range(1, n_digits):
            if str_i[k] != 0:
                recycled_i = int(str_i[k:] + str_i[:k])
                if recycled_i > i and recycled_i <= B:
                    pair_set.add("%d,%d" % (i, recycled_i))

        num_pairs += len(pair_set)

    return num_pairs

infile_name = sys.argv[1]

with open(infile_name, 'r') as infile:
    n_test_cases = int(infile.readline().strip())

    for i, line in enumerate(infile):
        i += 1
        if i > n_test_cases:
            break
        A, B = [int(r) for r in line.split()]
        num_pairs = find_recycled_pairs(A, B)
        print "Case #%d: %d" % (i, num_pairs)

