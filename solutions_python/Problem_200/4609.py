def is_tidy(number):
    numbers = [int(num) for num in str(number)]
    correct = True
    last = numbers[0]
    for num in numbers[1:]:
        if last > num:
            correct = False
        last = num
    return correct

def load_tests():
    tests = []
    with open('tidy_numbers_input.txt') as data:
        for line in data.readlines()[1:]:
            tests.append(int(line))
    return tests

def output(results):
    with open('tidy_numbers_output.txt', 'w+') as out:
        for i, line in enumerate(results):
            out.write('Case #{}: {}\n'.format(i+1, line))

def run_test(test):
    last = 0
    for number in range(test+1):
        if is_tidy(number):
            last = number
    return last

def main():
    tests = load_tests()
    results = []
    for test in tests:
        results.append(run_test(test))
    output(results)

main()
