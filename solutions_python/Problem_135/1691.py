import sys


BAD_MAGIC = 'Bad magician!'
CHEATER = 'Volunteer cheated!'


def parse_case(case):
    c1 = int(case[0])
    c2 = int(case[5]) + 5

    r1 = case[c1].split(" ")
    r2 = case[c2].split(" ")

    possibilities = list()

    for card1 in r1:
        if card1 in r2:
            possibilities.append(card1)

    if possibilities:
        if len(possibilities) == 1:
            result = possibilities[0]
        else:
            result = BAD_MAGIC
    else:
        result = CHEATER

    return result


def main():
    with open(sys.argv[1], 'rb') as fh:
        inp = fh.readlines()

    t = int(inp.pop(0))
    output = ''

    for i in range(t):
        result = parse_case([inp.pop(0).strip() for _ in range(10)])
        assert result is not None
        case = 'Case #%d: %s\r\n' % (i + 1, result)
        print case,
        output += case

    with open(sys.argv[1] + '.out', 'wb') as fh:
        fh.write(output)
    

if __name__ == '__main__':
    main()
