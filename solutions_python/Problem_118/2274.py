__author__ = 'sigito'

def square_palindromes(start, end):
    palindromes = set()

    exists = 0

    def is_palindrome(n):
        if not n in palindromes:
            n_str = str(n)
            if not all(n_str[i] == n_str[-(i + 1)] for i in range(len(n_str) // 2)):
                return False

            palindromes.add(n)

        return True

    from math import sqrt

    for n in range(end, start - 1, -1):
        # check if palindrome
        if not is_palindrome(n):
            continue

        # it is palindrome
        # get square
        sqrt_n = sqrt(n)

        if int(sqrt_n) != sqrt_n:
            continue

        # check if square is also a palindrome
        if not is_palindrome(int(sqrt_n)):
            continue

        exists += 1

    return exists


def solve():
    test_cases = read_int()
    for test_case in range(1, test_cases+1):
        ranges = read_tuple_of(int)
        existing_palindromes = square_palindromes(*ranges)
        print_case(test_case, existing_palindromes)


def test():
    assert square_palindromes(1, 4) == 2
    assert square_palindromes(10, 120) == 0
    assert square_palindromes(100, 1000) == 2


__author__ = 'sigito'


def read_int():
    """
    Reads int from input
    """
    return int(input())


def read_str():
    """
    Reads string from input
    """
    return input()


def read_list_of(type_cast, delimiter=' '):
    """
    Reads line from input and by splitting with `delimiter` and accepting `type_cast` on each element
    forms list. Empty split elements omitted.
    Raises ValueError if `type_cast` is not callable.
    """
    if not callable(type_cast):
        raise ValueError("type_cast must be a mapper function from string to needed type")

    return [type_cast(item) for item in input().split(delimiter) if item]


def read_tuple_of(type_cast, delimiter=' '):
    if not callable(type_cast):
        raise ValueError("type_cast must be a mapper function from string to needed type")

    return (type_cast(item) for item in input().split(delimiter) if item)


def print_case(case_index, parameter):
    """
    Prints to standard output "Case #`case_index`: `parameter`".
    """
    print("Case #{case_index}: {data}".format(case_index=case_index, data=parameter))


if __name__ == '__main__':
    solve()
