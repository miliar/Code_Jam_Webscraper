def parse(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    test_cases = int(lines[0])
    numbers = []
    for test in lines[1:test_cases+1]:
        numbers.append(test)

    return numbers

def is_increasing_number(str_number):
    if str_number[-1] == '\n':
        str_number = str_number[:-1]

    if len(str_number) == 1:
        return True

    test_number = int(str_number[0])
    for digit in map(int, str_number):
        if digit < test_number:
            return False
        test_number = digit
    return True

def save_result(filename, results):
    f = open(filename, 'w')
    for i, r in enumerate(results):
        if r[-1] == '\n':
            r = r[:-1]
        f.write('Case #{}: {}'.format(i+1, r))
        if i < len(results)-1:
            f.write('\n')
    f.close()


if __name__ == '__main__':
    str_numbers = parse('tidy_numbers.txt')
    print(is_increasing_number('123'))

    results = []
    for str_num in str_numbers:
        while(True):
            print(str_num)
            if is_increasing_number(str_num):
                print(str_num)
                results.append(str_num)
                break
            # Decrease
            str_num = str(int(str_num) - 1)

    save_result('tidy_numbers_result.txt', results)

