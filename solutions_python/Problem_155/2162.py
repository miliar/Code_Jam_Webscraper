def calculate(data):
    total = 0
    friends = 0
    for shyness, number in enumerate(map(int, data)):
        if shyness > total + friends:
            friends += shyness - (total + friends)
        total += number

    return friends


def main():
    input_file = open('A-large.in')
    output_file = open('A-large.out', 'w')
    cases = int(input_file.readline())
    for case in range(1, cases + 1):
        _, data = input_file.readline().split()
        solution = calculate(data)
        output_file.write('Case #{}: {}\n'.format(case, solution))
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
