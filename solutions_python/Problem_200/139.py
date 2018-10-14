def answer(n_str):
    digits = [ord(digit_char) - ord('0') for digit_char in n_str]
    digits_count = len(digits)

    last_digit = 9
    max_index = -1
    for i, digit in zip(reversed(range(digits_count)), reversed(digits)):
        if digit > last_digit:
            max_index = i
            digit -= 1
        last_digit = digit

    if max_index != -1:
        digits[max_index] -= 1
        for i in range(max_index + 1, digits_count):
            digits[i] = 9

    result = 0
    for digit in digits:
        result *= 10
        result += digit
    return str(result)


def main():
    t = int(input())
    for i in range(1, t + 1):
        n_str = input()
        print("Case #{}: {}".format(i, answer(n_str)))


if __name__ == "__main__":
    main()
