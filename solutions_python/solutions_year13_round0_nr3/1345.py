import math
import sys


def is_palindrome(s):
    result = True
    l = len(s)

    for i in range(len(s) / 2 + 1):
        if s[i] != s[l - i - 1]:
            result = False
            break

    return result


def count_f_sq(A, B):
    result = 0

    l = int(math.ceil(pow(A, 0.5)))
    r = int(math.floor(pow(B, 0.5)))

    for i in range(l, r + 1):
        if is_palindrome(str(i)) and is_palindrome(str(i * i)):
            result += 1

    return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        f_in = open("in.txt", "rt")
        f_out = sys.stdout
    else:
        f_in = open(sys.argv[1], "rt")
        f_out = open("out.txt", "wt")

    case_num = int(f_in.readline())

    for c in range(case_num):
        A, B = [int(x) for x in f_in.readline().split()]
        f_out.write("Case #%d: %d\n" % (c + 1, count_f_sq(A, B)))
    f_in.close()
    f_out.close()
