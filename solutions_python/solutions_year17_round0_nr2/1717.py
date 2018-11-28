import math

pows_of_ten = list(map(lambda x: int(10**x), range(19)))

def num_digits(n):
    return math.ceil(math.log(n, 10))

def nth_digit(n, x):
    return (x // pows_of_ten[n-1]) % 10

def is_tidy(n, l):
    last_digit = -1
    for i in range(l, 0, -1):
        d = nth_digit(i, n)
        if last_digit <= d:
            last_digit = d
        else:
            break
    else:
        return True
    return False


def fix(digits, i):
    ind = len(digits) - i - 1
    if digits[ind] >= digits[ind-1]:
        return digits
    return digits[:ind-1] + [digits[ind-1] - 1] + [9] * (i + 1)


if __name__ == "__main__":
    cases = int(raw_input())
    for case in range(1, cases+1):
        digits = map(int, raw_input())
        for i in range(len(digits) - 1):
            digits = fix(digits, i)
        print('Case #{}: {}'.format(case, int(''.join(map(str, digits)))))
