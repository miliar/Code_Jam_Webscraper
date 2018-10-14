def is_palindrome(string):
    """ (string) -> bool
    Return true if string is a palindrome

    >>> is_palindrome("a")
    True

    >>> is_palindrome("abc")
    False

    >>> is_palindrome("aba")
    True
    """
    if len(string) == 0:
        return False
    if len(string) == 1:
        return True
    if len(string) == 2 or len(string) == 3:
        return string[0] == string[-1]

    return is_palindrome(string[1:-1])


def fair_and_sqare(A, B):
    """ (num, num) -> int
    For numbers between A and B return the number of fair and square
    numbers (number is a palindrome and its square root is a palindrome)
    greater or equal to A and smaller or equal than B.

    >>> fair_and_sqare(1, 4)
    2

    >>> fair_and_sqare(10, 120)
    0

    >>> fair_and_sqare(100, 1000)
    2
    """
    counter = 0
    for i in range(A, B+1):
        if is_palindrome(str(i)):
            root = i**0.5
            if root == int(root) and is_palindrome(str(int(root))):
                            counter += 1
    return counter

if __name__ == '__main__':
    in_f = open("input.txt", "r")
    out_f = open("output.txt", "w")
    test_cases = int(in_f.readline())
    for case in range(test_cases):
        limits = in_f.readline().split()
        result = fair_and_sqare(int(limits[0]), int(limits[1]))
        out_f.write("Case #%d: %d\n" % (case+1, result))

    in_f.close()
    out_f.close()
