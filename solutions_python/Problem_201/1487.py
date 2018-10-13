import math


def get_result_from_stall_bank(num_stalls):
    half = (num_stalls - 1) / 2
    return [math.ceil(half), math.floor(half)]


def solve(left, right):
    if left is None:
        # print("Using right side")
        return right
    elif right is None:
        # print("Using left side")
        return left
    else:
        # print("Computing")
        return [min(left[0], right[0]), min(left[1], right[1])]


def run_people(stalls, people):
    # print("Running {} stalls for {} people".format(stalls, people))
    if people == 1:
        return get_result_from_stall_bank(stalls)

    if people == 0:
        # print("No people and {} stalls".format(stalls))
        return None

    if stalls == 0:
        print("HOW DID THIS HAPPEN!?")
        return None

    [my_max, my_min] = get_result_from_stall_bank(stalls)
    [more_people, less_people] = get_result_from_stall_bank(people)

    # Odd stalls is easy, divides by two after this person
    if stalls % 2 == 1:

        # If we have odd number of people thats even easier,
        # just run one side
        if people % 2 == 1:
            return run_people(my_max, more_people)

        # Even people with even stalls...
        # Send the extra person left
        else:
            left = run_people(my_max, more_people)
            right = run_people(my_min, less_people)
            return solve(left, right)

    # Even stalls means our max will actually be the right side
    else:

        # If we have odd number of people same people to both sides
        if people % 2 == 1:
            left = run_people(my_min, more_people)
            right = run_people(my_max, less_people)
            return solve(left, right)

        # Even people with even stalls...
        # Send the extra person right
        else:
            left = run_people(my_min, less_people)
            right = run_people(my_max, more_people)
            return solve(left, right)


def run_case(input):
    num_stalls, num_people = read_ints(input)

    out = run_people(num_stalls, num_people)
    return "{} {}".format(out[0], out[1])


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
