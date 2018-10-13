__author__ = 'dau'


def read(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except IOError:
        return None


def save(file_name, data):
    try:
        with open(file_name, 'w') as f:
            f.write(data)
    except IOError:
        return False
    else:
        return True


def minimum_guests(test):
    shyness = 0
    audience = 0
    guests = 0
    for digit in test:
        if digit > 0:
            if shyness > audience + guests:
                guests += shyness - (audience + guests)
            audience += int(digit)
        shyness += 1
    return guests


def solve(cases):
    solution = ''
    for t, test in enumerate(cases[1:], start=1):
        solution += 'Case #' + str(t) + ': ' + str(minimum_guests(test.split()[1])) + '\n'
    return solution


if __name__ == '__main__':
    problem_file_name = 'A-large.in'
    test_cases_lines = read(problem_file_name).strip().splitlines()
    save('solved_' + problem_file_name, solve(test_cases_lines))
