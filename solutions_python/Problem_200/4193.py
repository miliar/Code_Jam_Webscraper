def solve(numbers):
    for index, number in enumerate(numbers):
        if index == len(numbers) - 1:
            return numbers
        elif int(numbers[index+1]) < int(number):
            i = find_decreaseble_number(numbers[:index+1][::-1])
            ss = numbers[:i]
            if int(numbers[i]) - 1:
                ss += str(int(numbers[i]) - 1)
            for t in range(len(numbers) - i - 1):
                ss += '9'
            return ss


def find_decreaseble_number(numbers):
    for index, number in enumerate(numbers):
        if number != 0 and index+1 != len(numbers) and numbers[index+1] < number:
            return len(numbers) - index - 1
    return 0


with open('B-large.in', 'r') as r:
    with open('B-large.out', 'w') as w:
        c = int(r.readline())
        for i in range(c):
            numbers = r.readline().replace('\n', '')
            cc = solve(numbers)
            w.write('Case #{}: {}\n'.format(i+1, cc))