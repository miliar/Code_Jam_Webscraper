def check_if_number_is_tidy(input):
    """
    Checks if a given number is tidy or not
    :param input: 
    :return: Boolean
    """
    in_str = str(input)

    for i, c in enumerate(in_str):
        if i + 1 < len(in_str):
            c_now = int(c)
            c_next = int(in_str[i+1])
            if c_now > c_next:
                return False

    return True


def subtract_at_position(number, pos):
    """
    subtracts one from the number at given pos and adjusts accordingly
    :param number: reversed string of the given number
    :param pos: index of position where subtraction is to take place
    :return: 
    """
    num_list = list(number)
    if num_list[pos] == 0:
        raise ValueError("Trying to subtract from zero. It means logic is incorrect.")
    num_list[pos] = str(int(num_list[pos]) - 1)

    for i in range(pos):
        num_list[i] = "9"

    return "".join(num_list)


def solve(N):
    """
    Solve for large input
    :param N:
    :return:
    """
    N_str = str(N)
    N_str_reversed = N_str[::-1]

    for i, c in enumerate(N_str_reversed):
        if i != 0:  # skip the first
            if int(c) > int(N_str_reversed[i-1]):
                N_str_reversed = subtract_at_position(N_str_reversed, i)

    return int(N_str_reversed[::-1])


if __name__ == '__main__':
    testcases = int(input())

    for nth_case in range(1, testcases + 1):
        N = int(input())
        print("Case #%i: %s" % (nth_case, solve(N)))
