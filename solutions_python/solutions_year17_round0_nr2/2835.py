def tidy(input):
    lines = input.split('\n')
    lines.pop(0)
    for i, line in enumerate(lines):
        print 'Case #%d: %s' % (i+1, get_tidy(line))


def get_tidy(number):
    while ''.join(sorted(number)) != number:
        number = str(int(number) - 1)

    return number