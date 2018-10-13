import sys

def get_prev_tidy(n):
    """Get the greatest tidy integer no larger than n."""

    if n < 10:
        return n

    digits = []  # Digits in reverse order.
    while n > 0:
        quotient, rem = divmod(n, 10)
        digits.append(rem)
        n = quotient
        continue

    res = digits.pop()
    prev = res
    capped = True
    first_idx = len(digits) - 1
    for digit in reversed(digits):

        if capped:
            if digit >= prev:
                res = res * 10 + digit
                prev = digit
            else:
                res = get_prev_tidy(res - 1)
                res = res * 10 + 9
                capped = False
        else:
            res = res * 10 + 9

    return res


def main():
    """The main driver."""
    fp = open(sys.argv[1], 'r')
    for i, v in enumerate(fp):
        if i == 0:
            continue
        print('Case #{}: {}'.format(i, get_prev_tidy(int(v))))
        continue

    return 0


if __name__ == '__main__':
    main()

