def to_digits(n):
    return list(map(int, str(n)))


def from_digits(digits):
    return int("".join(map(str, digits)))


def is_tidy(digits):
    return all([digits[i] <= digits[i + 1] for i in range(len(digits) - 1)])


def largest_tidy(n):
    digits = to_digits(n)

    i = len(digits) - 2
    while not is_tidy(digits):
        if digits[i] > digits[i + 1]:
            digits[i] -= 1
            digits[i + 1:] = [9] * (len(digits) - 1 - i)
        i -= 1

    return from_digits(digits)


# print(to_digits(1234))
# print(is_tidy(to_digits(7)))
# print(is_tidy(to_digits(123)))
# print(is_tidy(to_digits(132)))
#
# print(largest_tidy(132))


# INPUT = "TestInput"
# OUTPUT = "TestOutput"

# INPUT = "SmallInput"
# OUTPUT = "SmallOutput"

INPUT = "LargeInput"
OUTPUT = "LargeOutput"


with open(INPUT, "r") as input_file:
    with open(OUTPUT, "w") as output_file:
        output_file.truncate()

        t = int(input_file.readline())
        for i in range(t):
            n = int(input_file.readline())
            tidy = largest_tidy(n)
            output_file.write(f"Case #{i+1}: " + str(tidy) + "\n")

