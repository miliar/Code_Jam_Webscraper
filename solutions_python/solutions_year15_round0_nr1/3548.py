__author__ = 'Gabe'


def det_min_friends(case):
    case = list(case)
    if case[-1] == '\n':
        case = case[:-1]
    smax = int(case[0])
    attendees = case[2:]
    attendees = map(int, attendees)
    assert(len(attendees) == smax + 1)

    run_sum = 0
    run_inject = 0
    for pos in xrange(len(attendees)):
        run_sum += attendees[pos]
        if pos >= run_sum:
            inject = pos + 1 - run_sum
            run_inject += inject
            run_sum += inject
    return run_inject

if __name__ == '__main__':
    with open('A-small-attempt0.in', 'r') as f:
        input_file = f.readlines()
        num_test_cases = int(input_file[0])
        test_cases = input_file[1:]
        assert len(test_cases) == num_test_cases
        min_friends = map(det_min_friends, test_cases)
        i = 0
        for min_friend in min_friends:
            i += 1
            print("Case #%d: %d" % (i, min_friend))