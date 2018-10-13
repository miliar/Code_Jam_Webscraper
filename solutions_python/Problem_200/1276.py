from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def tidy(n):
    if n < 10:
        return True

    while n > 1:
        n, k = divmod(n, 10)
        if n % 10 > k:
            return False

    return True


def digit2int(digits: list):
    intstr = "".join(map(str, digits))
    return int(intstr)


def int2digits(n):
    return [int(x) for x in str(n)]


def nozeros(n: int):
    digits = int2digits(n)
    while 0 in digits:
        zero = digits.index(0)
        # zero out all other digits greater than this
        digits = [digit if x < zero else 0 for x, digit in enumerate(digits)]
        n = digit2int(digits)
        n -= 1
        digits = int2digits(n)

    return n

    # for i, digit in enumerate(reversed(str(n))):
    #     if digit == "0":
    #         n -= 10 ** (i)
    #         break
    # else:
    #     return n
    # return nozeros(n)


# def solver(n):
#     # zeros are always bad!
#     n = nozeros(n)
#
#     # go from smallest to biggest
#     digits = [int(x) for x in reversed(str(n))]
#
#     for i, digit in enumerate(digits):
#         if i == len(digits) - 1:
#             break
#
#         if digit < digits[i + 1]:
#             digits[i + 1] -= 1
#             digits[i] = 9
#
#     ans = int("".join(map(str, reversed(digits))))
#     return ans


def solver(n):
    digits = int2digits(n)
    new = [digits[0]] + [(b if b >= a else 0) for a, b in pairwise(digits)]
    n = digit2int(new)
    return nozeros(n)

def solve(n):
    while not tidy(n):
        n = solver(n)

    return n

def brute(n):
    while not tidy(n):
        n -= 1

    return n

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        nn = int(input())
        answer = solve(nn)
        print(f"Case #{case}: {answer}")
