# Problem
#
# It's opening night at the opera, and your friend is the prima donna (the lead
# female singer). You will not be in the audience, but you want to make sure she
# receives a standing ovation -- with every audience member standing up and clapping
# their hands for her.
#
# Initially, the entire audience is seated. Everyone in the audience has a shyness
# level. An audience member with shyness level Si will wait until at least Si other
# audience members have already stood up to clap, and if so, she will immediately
# stand up and clap. If Si = 0, then the audience member will always stand up and
# clap immediately, regardless of what anyone else does. For example, an audience
# member with Si = 2 will be seated at the beginning, but will stand up to clap
# later after she sees at least two other people standing and clapping.
#
# You know the shyness level of everyone in the audience, and you are prepared to
# invite additional friends of the prima donna to be in the audience to ensure that
# everyone in the crowd stands up and claps in the end. Each of these friends may
# have any shyness value that you wish, not necessarily the same. What is the
# minimum number of friends that you need to invite to guarantee a standing ovation?

import sys


def get_data(file_name):
    """
        Get the data out of the input file.

        params:
            file_name - the path to the file to get the data from

        Input

        The first line of the input gives the number of test cases, T. T test
        cases follow. Each consists of one line with Smax, the maximum shyness
        level of the shyest person in the audience, followed by a string of
        Smax + 1 single digits. The kth digit of this string (counting starting
        from 0) represents how many people in the audience have shyness level k.
        For example, the string "409" would mean that there were four audience
        members with Si = 0 and nine audience members with Si = 2 (and none with
        Si = 1 or any other value). Note that there will initially always be
        between 0 and 9 people with each shyness level.

        The string will never end in a 0. Note that this implies that there will
        always be at least one person in the audience.
    """

    case = []
    with open(file_name) as f:
        num_cases = int(f.readline())

        for case_i in range(num_cases):
            line = f.readline()

            num_items = int(line.split(' ')[0]) + 1

            items = []
            in_data = line.split(' ')[1]
            for j in range(num_items):
                items += [int(in_data[j])]

            case += [items]

    return case


def solve(datum):
    """
        Solve a single problem.

        params:
            datum - list of items indicating the number of people in each tier

        returns: the minimum number of friends needed

        Output

        For each test case, output one line containing "Case #x: y", where x is
        the test case number (starting from 1) and y is the minimum number of
        friends you must invite.
    """
    total = 0
    extra = 0
    # print('\tSolving %s...' % datum)
    for index in range(len(datum)):
        if datum[index] > 0 and total < index:
            diff = index - total - extra
            extra += diff if diff > 0 else 0
        total += datum[index]
        # print('\t\tProcessing index %s, value %s: total: %s extra %s' %
        #         (index, datum[index], total, extra))
    return extra


def validate(datum, solution):
    """
        Validate a solution to the problem.

        params:
            datum - the input data
            solution - the solution to validate
    """

    total = solution
    for index in range(len(datum)):
        if total < index:
            print('\tInvalid solution! datum: %s' % datum)
            sys.exit(-1)
        total += datum[index]

if __name__ == '__main__':
    data = get_data(sys.argv[1])

    for i in range(len(data)):
        solution = solve(data[i])
        print("Case #%s: %s" % ((i + 1), solution))
        validate(data[i], solution)
