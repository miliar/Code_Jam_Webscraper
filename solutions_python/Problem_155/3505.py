

# read input
import fileinput

num_tests = -1
tests = []

for line in fileinput.input():
    line = line.strip()
    if num_tests == -1:
        num_tests = int(line)
        continue
    test_case = line.split()
    max_shy = test_case[0]  # Not sure I need this
    tests.append([int(d) for d in test_case[1]])  # char -> int


def solve(test):
    # for each member i check that there are at least i people with a higher
    # shyness level; this is classic recursive vs iterative and undoubtedly
    # has a smart mathematical solution that i am too fried to spot
    prev = 0
    extra = 0
    for index, a in enumerate(test):
        # check if we need any more at this i, to get these people to stand
        if index == 0:
            # we don't need anything
            pass
        elif a > 0:  # we don't care if there isn't anyone at this level
            # check how many people are standing up at shyness levels -> i-1
            if prev >= index:
                # we are good
                pass
            else:
                # we bribe the difference to show up and clap
                extra += index - prev
                prev += extra  # we now count them as being previous
                               # shyness levels
        # count how many are standing up to and including this level
        # so the next level is precomputed
        total_including_this_one = prev + a
        prev = total_including_this_one
    return extra

for index, test in enumerate(tests):
    result = solve(test)
    print "Case #{}: {}".format(index+1, result)
