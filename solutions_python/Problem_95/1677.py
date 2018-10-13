def main():
    with open('qual.input', 'r') as f:
        parsed = processCase(f.read())
        for (i, line) in enumerate(iter(parsed.splitlines())):
            if i is 0:
                continue
                #caseCount = line
            if i is 1:
                print 'Case #%s: %s' % (i, line.strip()),
            else:
                print '\nCase #%s: %s' % (i, line.strip()),


def processCase(line):
    return line\
    .replace('a', 'Y')\
    .replace('b', 'H')\
    .replace('c', 'E')\
    .replace('d', 'S')\
    .replace('e', 'O')\
    .replace('f', 'C')\
    .replace('g', 'V')\
    .replace('h', 'X')\
    .replace('i', 'D')\
    .replace('j', 'U')\
    .replace('k', 'I')\
    .replace('l', 'G')\
    .replace('m', 'L')\
    .replace('n', 'B')\
    .replace('o', 'K')\
    .replace('p', 'R')\
    .replace('q', 'Z')\
    .replace('r', 'T')\
    .replace('s', 'N')\
    .replace('t', 'W')\
    .replace('u', 'J')\
    .replace('v', 'P')\
    .replace('w', 'F')\
    .replace('x', 'M')\
    .replace('y', 'A')\
    .replace('z', 'Q')\
    .lower()

if __name__ == "__main__":
    main()
