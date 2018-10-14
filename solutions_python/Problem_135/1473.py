import sys


def read_m(f):
    m = []
    i = 0
    for l in f:
        i += 1
        row = map(int, filter(None, l.split()))
        m.append(row)
        if i == 4:
            break
    return m


def main():
    if len(sys.argv) > 1:
        inname = sys.argv[1]
    else:
        inname = 'test.in'
    outname = inname.replace('.in', '.out')
    with open(inname) as in_, open(outname, 'w') as out:
        t = int(in_.readline())

        for i in range(1, t+1):
            candidates = set()
            answer = int(in_.readline())
            matrix = read_m(in_)
            candidates.update(set(matrix[answer - 1]))
            answer = int(in_.readline())
            matrix = read_m(in_)
            candidates.intersection_update(set(matrix[answer - 1]))

            if len(candidates) == 0:
                guess = 'Volunteer cheated!'
            elif len(candidates) > 1:
                guess = 'Bad magician!'
            else:
                guess = str(next(iter(candidates)))
            out.write('Case #{}: {}\n'.format(i, guess))


if __name__ == '__main__':
    main()
