import math

file = 'C-small-attempt0'


def is_palindrome(number):
    n = str(number)
    first = int(math.floor(len(n) / 2))
    second = int(math.ceil(len(n) / 2)) + (0 if len(n) % 2 == 0 else 1)
    return n[0:first] == n[second:][::-1]

with open(file + '.in', 'r') as input:
    with open(file + '.out', 'w') as output:
        cases = int(input.readline())

        for case in range(0, cases):
            interval = tuple([int(x) for x in input.readline().strip().split(' ')])
            fair_square = 0

            for i in range(interval[0], interval[1] + 1):
                if is_palindrome(i):
                    sqrt = math.sqrt(i)

                    if int(sqrt) == sqrt and is_palindrome(int(sqrt)):
                        fair_square += 1

            output.write("Case #%d: %d\n" % (case + 1, fair_square))