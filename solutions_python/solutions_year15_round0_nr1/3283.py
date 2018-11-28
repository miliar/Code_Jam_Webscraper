__author__ = 'giel'

with open("input.txt") as input_file:
    T = int(input_file.readline())  # number of test cases
    test_cases = [l.strip() for l in input_file.readlines()]

for i, test_case in enumerate(test_cases):
    S_max, string = test_case.split()
    S_max = int(S_max)
    S_levels = map(int, list(string))
    needed = 0
    total = S_levels[0]
    for k in xrange(1, S_max+1):
        if k > total:
            newly_needed = k - total
            needed += newly_needed
            total += S_levels[k] + newly_needed
        else:
            total += S_levels[k]

    print "Case #%d: %d" % (i+1, needed)
