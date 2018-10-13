import sys
from math import sqrt
from math import floor
from math import ceil

def is_palindrome(x):
    s = x.split(".")[0]
    l = 0
    u = len(x) - 1
    while l <= u:
        if x[l] != x[u]:
            return False
        u -= 1
        l += 1
    return True


def count_palindromes(a, b):
    num = 0
    i = a - 1
    while i < b:
        i += 1
        i_str = str(i).split(".")[0]
        if not is_palindrome(i_str):
            continue

        ii = i * i
        ii_str = str(ii).split(".")[0]

        if is_palindrome(ii_str):
            num += 1

    return num


if __name__ == "__main__":
    num_testcases = int(sys.stdin.readline())
    for i in range(1, num_testcases + 1):
        tokens = sys.stdin.readline().split()
        a = float(tokens[0])
        b = float(tokens[1])
        a_sqrt = ceil(sqrt(a))
        b_sqrt = floor(sqrt(b))
        r = count_palindromes(a_sqrt, b_sqrt)
        print("Case #{n}: {r}".format(n=i, r=r))
