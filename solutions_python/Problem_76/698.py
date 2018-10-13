import sys
import string
import itertools

def patrick_add(a, b) :
    return (a | b) & ~(a & b)

def solve_case(case_num, n, values) :
    pairs = {}
    max_take = -1
    for num in xrange(1, n) :
        for i in itertools.combinations(values, num) :
            j = list(values)
            for entry in i :
                j.remove(entry)
            i_true_sum = sum(i)
            j_true_sum = sum(j)
            i_sum = reduce(patrick_add, i)
            j_sum = reduce(patrick_add, j)

            if (i_sum == j_sum) :
                max_take = max(max_take, i_true_sum, j_true_sum)

    if max_take == -1 :
        print "Case #%d: NO" % (case_num)
    else :
        print "Case #%d: %d" % (case_num, max_take)

data = file(sys.argv[1]).readlines()
pos = 0
num_cases = int(data[pos])
pos += 1

for case in xrange(num_cases) :
    n = int(data[pos])
    pos += 1
    values = [int(x) for x in string.split(data[pos], " ")]
    pos += 1
    solve_case(case + 1, n, values)
