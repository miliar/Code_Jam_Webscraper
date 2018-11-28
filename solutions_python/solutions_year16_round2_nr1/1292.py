from collections import Counter

def find_digit(identifier, digit_string, char_count):
    amount = char_count[identifier] / digit_string.count(identifier)
    for c in digit_string:
        char_count[c] -= amount

    return amount

def get_digits(line):
    digit_count = {}
    character_count = Counter(line)
    digits = [
        ("X", "SIX", 6),
        ("Z", "ZERO", 0),
        ("G", "EIGHT", 8),
        ("W", "TWO", 2),
        ("S", "SEVEN", 7),
        ("V", "FIVE", 5),
        ("F", "FOUR", 4),
        ("T", "THREE", 3),
        ("O", "ONE", 1),
        ("N", "NINE", 9)
    ]

    for (id_, digit_string, number) in digits:
        digit_count[number] = find_digit(id_, digit_string, character_count)

    return digit_count


def solve_testcase(line):
    digit_count = get_digits(line)
    result = ''
    for i in range(10):
        result += str(i) * int(digit_count[i])

    return result

def main():
    with open("large.in") as infile:
        infile.readline()
        for (i, line) in enumerate(infile, 1):
            print("Case #{}: {}".format(i, solve_testcase(line.strip())))


if __name__ == "__main__":
    main()
