import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_inputs():
    number = 0
    items = []
    with open(os.path.join(__location__, "input.txt")) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        number = int(content[0])
        for i in range(0, number):
            line = content[i+1]
            items.append(line)
    return number, items


#print(read_inputs())


def generate_tidy(number):
    if len(str(number)) == 1:
        return number
    digits = []
    for digit in str(number):
        digits.append(int(digit))

    i = 0
    # find first non increasing
    while i < len(digits) - 1 and digits[i] <= digits[i+1]:
        i += 1

    if i == len(digits)-1:
        return number

    # go backwards
    while i > 0 and digits[i] - 1 < digits[i-1]:
        i -= 1

    if i == 0 and digits[i] == 1:
        return pow(10, len(digits)-1) -1
    digits[i] -= 1
    for j in range(i+1, len(digits)):
        digits[j] = 9

    number = 0
    for digit in digits:
        number = number * 10 + digit
    return number


def tidy():
    number, inputs = read_inputs()
    for i in range(0, len(inputs)):
        print('Case #' +str((i+1))+':', generate_tidy(inputs[i]))

tidy()