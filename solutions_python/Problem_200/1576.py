def convert(digits):
    return int(''.join(str(dg) for dg in digits))


def solve():
    number = input()
    digits = [int(x) for x in number]
    index = len(digits) - 1
    changed_index = -1
    while index > 0:
        if digits[index] >= digits[index - 1]:
            index -= 1
            continue

        changed_index = index - 1
        digits[index - 1] -= 1
        index -= 1

    if changed_index == -1:
        return number

    for new_index in range(changed_index + 1, len(digits)):
        digits[new_index] = 9

    return convert(digits)


t = int(input())
for i in range(1, t + 1):
    result = solve()
    print("Case #{}: {}".format(i, result))
