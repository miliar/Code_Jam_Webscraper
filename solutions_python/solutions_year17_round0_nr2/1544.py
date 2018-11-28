def is_good(s):
    return ''.join(sorted(list(s))) == s


def count_down(N, pos):
    # set pos to one less than it used to be and all subsequent digits to 9
    old_digit = int(N[pos])
    if old_digit == 0:
        return False
    new_digit = old_digit - 1
    return "{}{}{}".format(
        N[:pos],
        new_digit,
        '9' * (len(N) - pos - 1))

def normalize(num_str):
    # Get rid of leading 0s
    return str(int(num_str))

def run_case(input):
    (N, ) = read_strs(input)

    if is_good(N):
        return normalize(N)

    pos = 1
    for pos in range(1, len(N)):
        if int(N[pos - 1]) <= int(N[pos]):
            continue
        else:
            break

    while pos >= 0:
        new_str = count_down(N, pos)
        if new_str == False:
            pos -= 1
            continue

        if is_good(new_str):
            return normalize(new_str)
        else:
            N = new_str

    return "WHOOPS"

##############################
#    CODE JAM BOILERPLATE    #
##############################


def read_ints(input, n=1):
    """ Read n integers from input - all on one line, space separated """
    return (int(st) for st in read_strs(input, n))


def read_strs(input, n=1):
    """ Read n strings from input - all on one line, space separated """
    return input.pop(0).rstrip("\n").split(" ")

# GCJ boiler plate...call run_case for each case given
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    lines = sys.stdin.readlines()
    sys.stdin = open('/dev/tty')
    num_cases = int(lines.pop(0))
    for case_num in range(num_cases):
        print("Case #{}: {}".format(case_num + 1, run_case(lines)))
