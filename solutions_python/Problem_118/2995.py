import math


def is_square(apositiveint):

    if apositiveint == 1:
        return True

    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False

        seen.add(x)

    return True


def is_palindrome(num):
    if len(str(num)) == 1:
        return True  # Single digit integers are palindromes by default
    else:
        num = str(num)
        if num == num[::-1]:
            return True

    return False

with open('in.txt', 'r+') as f:
    for index, line in enumerate(f):
        if index == 0:
            cases = line.strip()
        else:
            fairnsquare = 0
            a, b = line.strip().split(' ')
            for x in xrange(int(a), int(b) + 1):
                if is_square(x) and is_palindrome(x):
                    y = int(math.sqrt(x))
                    if is_palindrome(y):
                        fairnsquare += 1

            with open('out.txt', 'a+') as o:
                o.write('Case #%d: %d\n' % (index, fairnsquare))
