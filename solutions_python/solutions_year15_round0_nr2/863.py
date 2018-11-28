from math import ceil, sqrt


def run_case(input):
    """ Return string you want outputted. input is a file you can read from """
    num_diners = read_ints(input)
    plates = list(read_ints(input, num_diners))
    return run_list(plates)


def run_list(plates):
    """ Run a list of plates, return the duration and the resulting list """
    if len(plates) == 0:
        return 0

    plates = sorted(plates, reverse=True)
    highest_val = plates[0]

    if highest_val <= 3:
        return highest_val

    # start with the assumption they all eat
    cur_size = 1 + run_list([new - 1 for new in plates if new > 1])

    for to_move in range(2, ceil(highest_val / 2) + 1):
        new_size = run_list(
            [highest_val - to_move] + plates[1:] + [to_move])

        cur_size = min(cur_size, new_size + 1)

    return cur_size

##############################
# CODE JAM BOILERPLATE BELOW #
##############################


def read_ints(input, n=1):
    """ Read n integers from input - all on one line, space separated """
    return (int(st) for st in read_strs(input, n))


def read_strs(input, n=1):
    """ Read n strings from input - all on one line, space separated """
    return input.readline().rstrip("\n").split(" ")

# GCJ boiler plate...call run_case for each case given
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    with sys.stdin as f:
        for case_num in range(int(f.readline())):
            print("Case #%d: %s" % (case_num + 1, run_case(f)))
