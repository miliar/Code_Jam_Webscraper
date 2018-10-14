#####
# Code for Code Jam 2015 qualifier.
#####

import sys

DEBUG = False


def main():
    cases = []

    # Load data from stdin.
    for i in range(int(sys.stdin.readline())):
        case_data = sys.stdin.readline().rstrip("\n")
        try:
            case_shyness_levels = case_data.split(' ')[1]
        except IndexError:
            case_shyness_levels = []
        case = []
        for shyness_level in case_shyness_levels:
            case.append(int(shyness_level))
        cases.append(case)

    # Do the crunching!
    for case_n in range(len(cases)):
        # there are no people standing at the beginning of
        # the standing ovation.
        people_standing = 0
        extras = 0

        case = cases[case_n]
        debug("Case {}".format(case))
        for shyness_level in range(len(case)):
            debug("\tShyness level {}".format(shyness_level))
            # only bother if there are people on this shyness level
            # I really don't actually need this. It was just for better output.
            if case[shyness_level] > 0:
                debug("\t\tThere are {} person/s on this level.".format(
                    case[shyness_level]))
                debug("\t\tNeed {} person/s, we have {}".format(
                    shyness_level, people_standing))
                # Keep adding people (at the LAST shyness level) until we
                # have enough to make everyone on this shyness level stand up.
                while people_standing < shyness_level:
                    people_standing += 1
                    extras += 1
                    debug("\t\t\tAdding a stand-in...{} person/s".format(
                        people_standing))
                # The people stand!
                people_standing += case[shyness_level]

        print("Case #{}: {}".format(case_n + 1, extras))


def debug(msg):
    if DEBUG is True:
        print msg


if __name__ == '__main__':
    main()
