import sys

def magic(p1, c1, p2, c2):
    r1 = set(c1[p1-1])
    r2 = c2[p2-1]

    match = [x for x in r2 if x in r1]
    if match:
        if len(match) == 1:
            return match[0]
        return 'Bad magician!'
    return 'Volunteer cheated!'

def batch(data, size):
    for i in xrange(0, len(data), size):
        yield data[i:i+size]

def main():
    with open(sys.argv[1]) as f:
        lines = [l.rstrip() for l in f.readlines()]

    for i, group in enumerate(batch(lines[1:], 10), 1):
        p1 = int(group[0])
        p2 = int(group[5])
        c1 = [[int(x) for x in row.split()] for row in group[1:5]]
        c2 = [[int(x) for x in row.split()] for row in group[6:10]]

        print 'Case #{0}: {1}'.format(i, magic(p1, c1, p2, c2))

if __name__ == '__main__':
    main()
