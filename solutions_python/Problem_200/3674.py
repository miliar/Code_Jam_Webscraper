def is_tidy(number_string):
    if len(number_string) == 1:
        return True

    previous_digit = number_string[0]

    for i in range(1, len(number_string)):
        if int(previous_digit) > int(number_string[i]):
            return False

    return True

t = int(raw_input())
f = open('out', 'w')

for j in xrange(1, t + 1):
    number = raw_input()

    for i in range(len(number) - 1):
        digits = number[len(number) - i - 1:len(number)]
        if not is_tidy(digits):
            if digits[0] != "0":
                new_digits = str(int(digits[0]) - 1) + "9" * (len(digits) - 1)
                number = number[:len(number) - i - 1] + new_digits

    if not is_tidy(number):
        if number[0] == "0":
            number = "9" * (len(number) - 1)
        else:
            number = str(int(number[0]) - 1) + ("9" * (len(number) - 1))

    f.write("Case #{}: {}\n".format(j, int(number)))

f.close()
