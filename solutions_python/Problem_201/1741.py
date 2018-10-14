INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def solve(n, k):

    pieces = [n]

    for i in xrange(k):

        m = max(pieces)
        j = pieces.index(m)

        if m % 2 == 1:
            new = (m-1) / 2
            pieces[j:j+1] = [new, new]
        else:
            new = m/2
            pieces[j:j+1] = [new - 1, new]

        if i == k-1:
            if m % 2 == 1:
                new = m / 2
                return str(new), str(new)
            else:
                new = m / 2
                return str(new), str(new - 1)


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as g:
        for i, line in enumerate(f):
            if i == 0:
                continue
            n, k = map(int, line.strip().split())
            outline = 'Case #{i}: {soln}\n'.format(i=i, soln=' '.join(solve(n, k)))
            g.write(outline)
            print outline,


if __name__ == '__main__':
    main()
