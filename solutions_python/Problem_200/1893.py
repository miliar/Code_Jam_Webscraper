
def read_lines():
    with open('test.input') as f:
        return f.readlines()

# 1537 -> 1499
def solve(number):
    i = 0
    while (i < len(number) - 1):
        print(number)
        print(i)
        print(number[i])
        print(number[i + 1])

        if (number[i] > number[i + 1]):
            number[i] = str(int(number[i]) - 1)
            print(number)
            fill_with_9(number, i + 1)
            print(number)
            i = max(i - 2, -1)
            # print(i)
            # handle 00 case
        i += 1

    return ''.join(str(e) for e in number).lstrip('0')

def fill_with_9(line, start):
    while (start < len(line)):
        line[start] = "9"
        start += 1

def iterate(n, lines):
    res = ''
    for i in range(n):
        res += "Case #" + str(i + 1) + ": " + solve(list(lines[i])) + '\n'

    print(res)
    with open('result.txt', 'w') as f:
        f.write(res)


if __name__ == '__main__':
    lines = list(map(lambda x: x.strip(), read_lines()))
    # iterate(1, ['886'])
    iterate(int(lines[0]), lines[1:])
