

def last_tidy(number):
    digits = [int(x) for x in str(number)]
    count = 0
    while not is_tidy(digits):
        count = count + 1
        num_digits = len(digits)
        # print 'testing {}'.format(digits)
        for i in range(num_digits - 1):
            digit = digits[num_digits - 1 - i]
            prev_digit = digits[num_digits - 2 - i]
            if digit < prev_digit:
                # print digit, prev_digit
                prev_digits = digits[:num_digits - 1 - i]
                # print prev_digits
                prev_number = int(''.join(str(d) for d in prev_digits))
                # print prev_number
                next_prefix = prev_number - 1
                # print next_prefix
                next_prefix_digits = [int(x) for x in str(next_prefix)]
                # print next_prefix_digits
                digits = next_prefix_digits + ([9] * (i + 1))
                break
    return int(''.join(str(d) for d in digits))


def is_tidy(digits):
    last_digit = 0
    for x in digits:
        if x >= last_digit:
            last_digit = x
        else:
            return False
    return True


