import sys


def decrease_digit(digits, index):
    if digits[index] != digits[index-1]:
        digits[index] -= 1
        index += 1
    else:
        return decrease_digit(digits, index-1)

    # go back over as many 1's as possible
    # i -= 1
    # while i >= 0 and digits[i] == 1:
    #     i -= 1
    #
    # digits[i] -= 1
    # i += 1
    return digits, index


def solve(line):
    digits = [int(a) for a in list("0" + line.strip())]

    i = 0
    place = len(digits)
    while i < len(digits):
        if i != len(digits)-1 and digits[i] > digits[i+1]:
            digits, place = decrease_digit(digits, i)
            print >> sys.stderr, digits, place
            break

        i+=1

    while place < len(digits):
        digits[place] = 9
        place+=1

    print >> sys.stderr, digits

    return int(''.join(str(x) for x in digits))


if __name__ == "__main__":
    inp = sys.stdin.readlines()
    inp = inp[1:]

    T = len(inp)

    for i, input_line in enumerate(inp):
        ans = solve(input_line)
        ans = "Case #{}: {}".format(i+1, ans)
        print ans
        print >> sys.stderr, ans
