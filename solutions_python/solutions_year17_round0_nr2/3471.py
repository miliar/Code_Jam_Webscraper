def main():
    second_attempt()

def first_attempt():
    output_string = 'Case #{}: {}'
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        n = int(input())
        while not check(n):
            # need a faster way of decreasing
            n -= 1
        print(output_string.format(case, n))

def second_attempt():
    output_string = 'Case #{}: {}'
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        n = int(input())
        digits = split_digits(n)
        while not check(join_digits(digits)):
            last_digit = 0
            for place, digit in enumerate(digits):
                if digit < last_digit:
                    digits[place - 1] -= 1
                    digits[place:] = [9] * (len(digits) - place)
                    break
                last_digit = digit
        print(output_string.format(case, join_digits(digits)))

def join_digits(digits):
    n = 0
    for digit in digits:
        n *= 10
        n += digit
    return n

def split_digits(n):
    output = []
    while n:
        output.append(n % 10)
        n //= 10
    return output[::-1]

def check(number):
    last_digit = 9
    while number:
        this_digit = number % 10
        if this_digit > last_digit:
            return False
        number //= 10
        last_digit = this_digit
    return True



if __name__ == '__main__':
    main()
