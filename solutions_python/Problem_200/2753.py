from fileinput import input

data = input('B-large.in')

for case in range(int(next(data))):
    number = list(map(int, next(data).strip()))
    for i in range(len(number) - 1, 0, -1):
        if number[i] < number[i - 1]:
            number[i - 1] -= 1
            for j in range(i, len(number)):
                number[j] = 9

    k = 0
    while number[k] == 0:
        k += 1

    print(
        'Case #{}: {}'.format(
            case + 1,
            ''.join(map(str, number[k:]))))

