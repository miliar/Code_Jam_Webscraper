def brute_force_solution(n):
    def is_non_decreasing(k):
        last_digit = k % 10
        k //= 10

        while k != 0:
            digit = k % 10
            k //= 10

            if not digit <= last_digit:
                return False

            last_digit = digit

        return True

    while not is_non_decreasing(n):
        n -= 1

    return n


def smart_solution(n):
    base10_digits = [i for i in range(10)]

    # Turning n into a series of digits in reverse for easier manipulation:
    n_digits = []
    while n > 0:
        n_digits.append(n % 10)
        n //= 10

    def borrow(i_digit):
        new_digit_val = base10_digits[n_digits[i_digit] - 1]

        if new_digit_val > n_digits[i_digit]:
            borrow(i_digit + 1)

        n_digits[i_digit] = new_digit_val

    repeat = True

    while repeat:
        repeat = False

        for i_l in range(len(n_digits) - 1):
            i_r = i_l + 1

            l = n_digits[i_l]
            r = n_digits[i_r]

            if l < r:
                # Non-decreasing! Must rectify!
                borrow(i_r)

                for i in range(i_l + 1):
                    n_digits[i] = 9

                repeat = True

                # else:
                #     n_digits[i_l] = base10_digits[n_digits[i_l - 1]]

    # Converting back to a number:
    n_digits.reverse()
    op_n = 0
    for d in n_digits:
        op_n = (op_n * 10) + d

    return op_n


if __name__ == '__main__':
    t = int(input())

    with open('output_b.txt', 'w') as f:
        for i_t in range(t):
            solution = smart_solution(int(input()))
            print('Case #{}: {}'.format(i_t + 1, solution), file=f)
