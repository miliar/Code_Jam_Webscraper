def read_floats(file):
    line = file.readline().strip().split()
    result = tuple(map(float, line))
    if len(result) == 1:
        result = result[0]
    return result


def input():
    filename = __file__.split('.')[0] + '.in'
    with open(filename) as file:
        tests_count = int(file.readline().strip())

        for test_index in xrange(tests_count):
            c, f, x = read_floats(file)
            yield c, f, x


def output():
    filename = __file__.split('.')[0] + '.out'
    with open(filename, 'w') as file:
        i = 0
        while True:
            value = (yield)
            i += 1
            file.write('Case #%d: %.7f\n' % (i, value))


def main():
    results = output()
    results.next()

    for task in input():
        c, f, x = task
        speed = 2.

        answer = x / speed
        time = 0.
        while time < answer:
            time += c / speed
            speed += f
            answer = min(answer, time + x / speed)

        results.send(answer)

    results.close()

if __name__ == '__main__':
    main()
