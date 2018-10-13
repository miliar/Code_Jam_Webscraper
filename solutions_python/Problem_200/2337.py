def last_tidy(n_digits, pos, last_dec):
    if pos < 0:
        return n_digits
    else:
        decrease = False
        for i in range(pos + 1, max(len(n_digits), last_dec)):
            if n_digits[pos] > n_digits[i]:
                decrease = True
                last_dec = pos
                break
        if decrease:
            for i in range(pos + 1, len(n_digits)):
                n_digits[i] = 9

            n_digits[pos] -= 1

        return last_tidy(n_digits, pos - 1, last_dec)


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        n_digits = [int(d) for d in str(n)]
        tidy_digits = last_tidy(n_digits, len(n_digits) - 1, -1)
        tidy = int(''.join([str(d) for d in tidy_digits]))

        print('Case #{}: {}'.format(i, tidy))

if __name__ == '__main__':
    main()