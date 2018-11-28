# *-* coding:utf-8 *-*


def main_result(input):
    digits = []
    m = 0
    if input == 0:
        return "INSOMNIA"
    while len(digits) < 10:
        m += 1
        for s in str(input * m):
            if s not in digits:
                digits.append(s)

    return input * m


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    # n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    n = int(raw_input())
    result = main_result(n)
    print "Case #{}: {}".format(i, result)



