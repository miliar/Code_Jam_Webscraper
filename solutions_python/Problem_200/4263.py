def solve(number):
    idx = -1
    number = [int(x) for x in number]
    for ii in range(len(number) - 1):
        if number[ii] > number[ii + 1]:
            idx = ii
            break
    if idx == -1:
        return ''.join([str(x) for x in number])

    if idx == 0:
        number[idx] -= 1

    for ii in range(idx + 1, len(number)):
        number[ii] = 9

    while idx > 0:
        number[idx] -= 1
        if number[idx] < number[idx - 1]:
            number[idx] = 9
            number[idx - 1] -= 1
            idx -= 1
        else:
            break

    if number[0] == 0:
        return ''.join([str(x) for x in number[1:]])
    else:
        return ''.join([str(x) for x in number])


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        number = input()
        result = solve(number)
        print("Case #{}: {}".format(i, result))
