def get_tidy(n):
    number = n
    while True:
        digits = [int(digit) for digit in str(number)]
        all_good = True
        for index in range(len(digits) - 1):
            if digits[index] > digits[index + 1]:
                digits[index] -= 1
                for sub_index in range(index + 1, len(digits)):
                    digits[sub_index] = 9
                all_good = False
                break
        if all_good:
            return number
        number = int("".join([str(digit) for digit in digits]))


for index in range(1, int(input()) + 1):
    n = int(input())
    print("Case #%s: %s" % (index, get_tidy(n)))
