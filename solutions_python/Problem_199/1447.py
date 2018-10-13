def flip(char):
    if char == '+':
        return '-'
    else:
        return '+'


def all_happy(pancakes):
    return all(c == '+' for c in pancakes)


def all_sad(pancakes):
    return all(c == '-' for c in pancakes)


def flips_required(pancakes, K, flips_so_far=0):
    # print("Checking {}".format(pancakes))
    if len(pancakes) <= K:
        if all_happy(pancakes):
            return flips_so_far, True
        elif all_sad(pancakes):
            return flips_so_far + 1, True
        else:
            return flips_so_far, False

    if pancakes[0] == '+':
        return flips_required(pancakes[1:], K, flips_so_far)

    flipped_front = ''
    for i in range(1, K):
        flipped_front += flip(pancakes[i])

    return flips_required("{}{}".format(
        flipped_front, pancakes[K:]), K, flips_so_far + 1)


def run_case(input):
    pancakes, K = read_strs(input)
    K = int(K)
    flips, possible = flips_required(pancakes, K)
    if possible:
        return flips
    else:
        return 'IMPOSSIBLE'

##############################
#    CODE JAM BOILERPLATE    #
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
            print("Case #{}: {}".format(case_num + 1, run_case(f)))
