def get_digits(n):
    while n > 0:
        yield n % 10
        n //= 10


def make_tidy(n):
    rev_digits = [digit for digit in get_digits(n)]  # in reverse order
    index = 0
    last_set = -1 # optimization to keep track of last num set to 9
    while index < len(rev_digits) - 1:
        if rev_digits[index] < rev_digits[index + 1]:
            # set all numbers up to and including cur to 9
            for i in range(last_set + 1, index + 1):
                rev_digits[i] = 9
            last_set = index
            # decrement next num by 1
            rev_digits[index + 1] -= 1
        index += 1

    # recreate number
    num = 0
    for dig_idx in range(len(rev_digits) - 1, -1, -1):
        num *= 10
        num += rev_digits[dig_idx]

    return num


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        print("Case #%d: %d" % (i, make_tidy(N)))
