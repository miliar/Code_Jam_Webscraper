def rightmost_bad(digits):
    for i in range(len(digits) - 1):
        digit = digits[-2 - i]
        next_digit = digits[-1 - i]
        if digit > next_digit:
            return len(digits) - 2 - i
    return None

def is_tidy(digits):
    for i in range(1, len(digits)):
        if digits[i] < digits[i - 1]:
            return False
    return True

def largest_tidy(n):
    digits = [int(digit) for digit in list(str(n))]
    # Count down until we find one?
    # Would not work for large numbers, e.g. 998877665544332211

    # Decrease the rightmost digit with a greater digit to its right.
    # If this digit is the leftmost digit and it's currently a 1,
    # then remove that digit and make the rest nines.
    # This should be quick.
    # Actually, we should rollover even if it's not the rightmost digit.
    # Actually, we should always rollover.

    while(not is_tidy(digits)):
        rightmost_bad_index = rightmost_bad(digits)
        rightmost_bad_digit = digits[rightmost_bad_index]

        digits[rightmost_bad_index] = rightmost_bad_digit - 1
        for i in range(rightmost_bad_index + 1, len(digits)):
            digits[i] = 9

    return int(''.join([str(digit) for digit in digits]))


num_cases = int(input())

for i in range(num_cases):
    result = largest_tidy(int(input()))
    if is_tidy([int(digit) for digit in list(str(result))]):
        print("Case #" + str(i + 1) + ": " + str(result))
    else:
        print("ERROR: bad result! " + str(result) + " is not tidy!")
