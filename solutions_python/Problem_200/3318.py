def solve_case(n):
    """Solve a test case n.

    Find the largest number smaller than n where all digits are in non-
    decreasing order."""
    while True:
        n_as_list = list(str(n))
        if sorted(n_as_list) == n_as_list:
            return n
        else:
            n -= 1


def main():
    test_cases = (int(input()) for __ in range(int(input())))
    for i, solved in ((i+1, solve_case(n)) for i, n in enumerate(test_cases)):
        print('Case #{i}: {solved}'.format(i=i, solved=solved))


if __name__ == '__main__':
    main()