def run_case(input):
    """ Return string you want outputted. input is a file you can read from """
    _, shyness = read_strs(input, 2)
    total_standing = 0
    total_needed = 0
    for i in range(len(shyness) - 1):
        to_stand = int(shyness[i])
        total_standing += to_stand

        need_to_add = max(0, i + 1 - total_standing)
        total_needed += need_to_add
        total_standing += need_to_add

    return total_needed


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
