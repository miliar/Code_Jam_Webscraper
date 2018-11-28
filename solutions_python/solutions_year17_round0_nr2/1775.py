import sys


def digits_to_int(digits):
    return int(''.join(map(str, digits)))


def split_to_digits(int_or_str):
    return [int(i) for i in str(int_or_str)]


def get_untidy_pos(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return i + 1

    return None


def tidy_number(digits):
    split_at = get_untidy_pos(digits)

    while split_at is not None:
        digits[split_at:] = [9] * (len(digits) - split_at)  # Set all following digits to 9
        digits[:split_at] = split_to_digits(digits_to_int(digits[:split_at]) - 1)  # Subtract 1 from digits[:split_at]
        split_at = get_untidy_pos(digits)

    return digits


for index, line in enumerate(sys.stdin):
    if index == 0:
        continue

    digits = split_to_digits(line.strip())
    tidy = digits_to_int(tidy_number(digits))
    print(f'Case #{index}: {tidy}')
