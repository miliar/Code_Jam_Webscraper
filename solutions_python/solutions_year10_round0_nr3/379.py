import sys

def one_ride(constants, state, hist):
    seats, gs = constants
    rides_left, first_in_line, earned = state

    if first_in_line in hist:
       (h_rides_left, h_earned) = hist[first_in_line]
       rides_in_cycle = h_rides_left - rides_left
       earned_in_cycle = earned - h_earned
       cycles_left = rides_left / rides_in_cycle
       rides_left -= cycles_left * rides_in_cycle
       earned += cycles_left * earned_in_cycle
       if (rides_left == 0):
           return (rides_left, first_in_line, earned)
    else:
       hist[first_in_line] = (rides_left, earned)

    space_left = seats
    groups_on_train = 0
    while gs[first_in_line] <= space_left and groups_on_train < len(gs):
       space_left -= gs[first_in_line]
       first_in_line += 1
       first_in_line %= len(gs)
       groups_on_train += 1
    earned += seats - space_left

    return (rides_left-1, first_in_line, earned)

def earning_better(R, k, gs):
    """
    >>> earning_better(4, 6, [1, 4, 2, 1])
    21
    """
    constants = k, gs
    state = R, 0, 0
    hist = {}
    while state[0] != 0:
        state = one_ride(constants, state, hist)
    return state[-1]

def earning_naive(R, k, gs):
    """
    >>> earning_naive(4, 6, [1, 4, 2, 1])
    21
    """
    earned = 0
    first_in_line = 0
    for _ in xrange(R):
        space_left = k
        groups_on_train = 0
        while gs[first_in_line] <= space_left and groups_on_train < len(gs):
            space_left -= gs[first_in_line]
            first_in_line += 1
            first_in_line %= len(gs)
            groups_on_train += 1
        earned += k - space_left
    return earned

def do_one_test_case(file):
    R, k, N = (int(n) for n in file.readline().split())
    gs = [int(n) for n in file.readline().split()]
    #e = earning_naive(R, k, gs)
    e = earning_better(R, k, gs)
    return e

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline())
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = expected_list[0:-1]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)
