def pancakes(input):
    lines = input.split('\n')
    lines.pop(0)
    for i, line in enumerate(lines):
        params = line.split(' ')
        answer = happy([True if x == '+' else False for x in params[0]], int(params[1]))
        print 'Case #%d: %s' % (i+1, answer)


def happy(cakes, size):
    if all(cakes):
        return 0

    if size > len(cakes):
        return 'IMPOSSIBLE'

    steps = 0
    while not all(cakes):
        start = cakes.index(False)
        if start + size > len(cakes):
            return 'IMPOSSIBLE'

        for i in range(start, start + size):
            cakes[i] = not cakes[i]
        steps += 1

    return steps

pancakes(input)