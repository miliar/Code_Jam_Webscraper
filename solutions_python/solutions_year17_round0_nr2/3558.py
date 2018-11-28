def transform(num, up=2):
    """
    Transform a number like this:
    234999876
          869
         9799
         8999
        98999
       899999
    234899999

    To make it a tidy number.

    >>> transform(234999876)
    234899999

    Further, these cases also need to be transformed:

    >>> transform(10000000000009)
    9999999999999

    So do these
    >>> transform(120009)
    119999
    """

    # get the length of the integer
    length_of_int = len(str(num))

    # if the upper bound is larger than length of integer
    if up > length_of_int:
        return num

    # get the digits compared
    next_digit = digit(num, up)
    last_digit = digit(num, up - 1)

    # if the next digit is bigger than the last digit
    if next_digit >= last_digit:

        # find replacement
        replacement = (next_digit) * 10**(up - 1) - 1

        # reconstruct the number and do transformation
        # again
        new_number = num - (num % 10**(up)) + replacement

        if not is_tidy(new_number):
            new_number = transform(new_number, up + 1)

    elif not is_tidy(num):

        # read prev digit
        prev_digit = digit(num, up - 1)

        if next_digit > prev_digit:
            replacement = (next_digit) * 10**(up - 1) - 1
            new_number = num - (num % 10**(up)) + replacement
        else:
            new_number = transform(num, up + 1)

    return new_number


def check_equal(num, compare):
    """
    Return True if all digits of number are the same,
    False otherwise.
    """

    num_str = str(num)
    compare_str = str(compare)

    if len(num_str) == 1:
        return num == compare

    elif len(num_str) == 2:
        return num_str[0] == num_str[1]

    elif num_str[0] == num_str[-1] == compare_str:
            return check_equal(num_str[1:-1], compare_str)

    else:
        return False


def tidy_number(num):
    """ (int) -> int
    Given an integer, return the last tidy number counted

    >>> tidy_number(132)
    129
    >>> tidy_number(1000)
    999
    >>> tidy_number(7)
    7
    >>> tidy_number(1234598765)
    1234589999
    """
    # if number is already tidy, return the number
    if is_tidy(num):
        return num

    # if number is not tidy
    else:

        new_num = transform(num)

        return new_num


def digit(number, place):
    """ (int, int) -> int
    Return the place of given number.
    """
    return number // 10**(place - 1) % 10


def is_tidy(num):
    """ (int) -> bool
    Returns True if int is tidy, False otherwise.
    """
    # if length is 1
    if len(str(num)) == 1:
        return True

    # if length is >= 2
    elif len(str(num)) >= 2:

        # compare last two digits
        last_digit = digit(num, 1)
        second_last_digit = digit(num, 2)

        # if this isn't tidy, then return False
        if second_last_digit > last_digit:
            return False
        else:

            # trim last character
            return is_tidy(num // 10)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
if __name__ == "__main__":
    t = int(input())  # read a line with a single integer

    for i in range(1, t + 1):

        # read the letter
        n = int(input())

        print("Case #{}: {}".format(i, tidy_number(n)))
        # check out .format's specification for more formatting options

