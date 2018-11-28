def number_from_digits(digits):
    # remove 0s in the beginning
    index = 0
    while index < len(digits) and digits[index] == 0:
        index += 1
    digits = digits[index:]

    result = 0
    for digit in digits:
        result = result * 10 + digit
    return result


def solve(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            digits[i] = digits[i] - 1
            for j in range(i + 1, len(digits)):
                digits[j] = 9
                
    return number_from_digits(digits)


t = int(input())
for t_count in range(1, t + 1):
    n = int(input())
    print("Case #{0}: {1}".format(t_count, solve(n)))
