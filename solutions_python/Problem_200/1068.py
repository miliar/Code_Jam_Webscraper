__author__ = 'User'


def highest_tidy_number(digits):
    for i in range(len(digits) - 1, 0, -1):
        if int(digits[i]) < int(digits[i-1]):
            digits[i-1] = str(int(digits[i-1]) - 1)
            digits[i:] = ['9'] * len(digits[i:])
    if len(digits) > 1 and digits[0] == '0':
        digits = digits[1:]
    return ''.join(digits)

with open("input.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            # line, k = line.split(" ")
            x = highest_tidy_number(list(line.strip()))
            write_file.write("Case #" + str(i) + ": " + str(x) + "\n")