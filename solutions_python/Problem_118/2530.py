__author__ = 'pard'


def _is_palindrome(integer):
    num_as_string = str(integer)
    return num_as_string == num_as_string[::-1]


def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_square(apositiveint):
    x = apositiveint // 2
    seen = {x}
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def algorithm(string):
    range = string.split()
    count = 0
    for i in xrange(int(range[0]), int(range[1])+1):
        if i == 1:
            count += 1
        elif _is_palindrome(i) and is_square(i):
            if _is_palindrome(isqrt(i)):
                count += 1
    return str(count)