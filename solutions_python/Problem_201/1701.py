import math


def recur(n, k):
    # if k > math.ceil(n/2.0):
    #     return 0, 0

    big_half = long(math.ceil((n-1)/2.0))
    small_half = long(math.floor((n-1)/2.0))
    if k == 1:
        return long(big_half), long(small_half)

    remaining = k-1
    if remaining % 2 == 0:
        # small half
        return recur(small_half, remaining/2)
    else:
        # big half
        return recur(big_half, long(math.ceil(remaining/2.0)))


def solve(n, k):
    maximum, minimum = recur(n, k)
    return "{} {}".format(maximum, minimum)


def main():
    num_cases = int(raw_input())

    for case_index in range(num_cases):
        case_line = raw_input()
        n, k = [long(x) for x in case_line.split(' ')]

        answer = solve(n, k)

        print("Case #{}: {}".format(case_index+1, answer))

main()
