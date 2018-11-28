import sys


def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for i in range(nr_cases):
            l, x = map(int, fp.readline().split())
            chars = fp.readline().strip()
            cases.append(x * chars)
    return cases


def mult(x, y):
    if x == '1':
        return y
    elif y == '1':
        return x
    elif x == 'i' and y == 'i':
        return '-1'
    elif x == 'i' and y == 'j':
        return 'k'
    elif x == 'i' and y == 'k':
        return '-j'
    elif x == 'j' and y == 'i':
        return '-k'
    elif x == 'j' and y == 'j':
        return '-1'
    elif x == 'j' and y == 'k':
        return 'i'
    elif x == 'k' and y == 'i':
        return 'j'
    elif x == 'k' and y == 'j':
        return '-i'
    elif x == 'k' and y == 'k':
        return '-1'


def solve(cases):
    output = ''
    for i, c in enumerate(cases):
        # print c
        res = 'NO'
        solution = ''
        target = 'i'
        negs = 0
        while True:
            # print c[0]
            if c[0] == target:
                solution += target
                # print "target", target
                c = c[1:]
                if target == 'i':
                    target = 'j'
                elif target == 'j':
                    target = 'k'
                elif target == 'k':
                    target = None

                # print "solution", solution
                # print "target", target
                if c == '':
                    break
                continue

            if len(c) > 1:
                new = mult(c[0], c[1])
                # print c[0], c[1], "=>", new
                if new.startswith('-'):
                    negs += 1
                    new = new.strip('-')
                c = new + c[2:]
            else:
                if c != '1':
                    solution += c
                break
        if (negs % 2) != 0:
            solution += '-'

        print "final", solution
        if solution == 'ijk':
            res = 'YES'
        output += 'Case #%d: %s\n' % (i+1,  res)
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)
    output = solve(cases)

    with open(out, 'w') as fp:
        fp.write(output)
