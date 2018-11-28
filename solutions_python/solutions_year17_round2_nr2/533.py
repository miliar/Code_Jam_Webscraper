INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def place(nc1, c1, nc2, c2, previous, first, stalls, i):
    if previous == c1:
        stalls[i] = c2
        previous = c2
        nc2 -= 1
    elif nc1 > nc2:
        stalls[i] = c1
        previous = c1
        nc1 -= 1
    elif previous == c2:
        stalls[i] = c1
        previous = c1
        nc1 -= 1
    elif first == c1:
        stalls[i] = c2
        previous = c2
        nc2 -= 1
    else:
        stalls[i] = c1
        previous = c1
        nc1 -= 1

    return nc1, nc2, previous, stalls


def smallsolve(n, r, y, b):
    n = float(n)
    if r/n > 0.5 or y/n > 0.5 or b/n > 0.5:
        return "IMPOSSIBLE"

    stalls = [None]*int(n)
    previous = None
    remainder = ''
    for i in xrange(int(n)):
        first = stalls[0]
        if b == r == y:
            if 'B' == first:
                if 'B' == previous:
                    remainder = 'RBY'*b
                else:
                    remainder = 'BRY'*b
            elif 'R' == first:
                if 'B' == previous:
                    remainder = 'RBY'*b
                else:
                    remainder = 'BRY'*b
            else:
                if 'B' == previous:
                    remainder = 'YBR'*b
                else:
                    remainder = 'BYR'*b
            stalls = stalls[:i]
            break
        elif b >= r >= y:
            b, r, previous, stalls = place(b, 'B', r, 'R', previous, first, stalls, i)
        elif b >= y >= r:
            b, y, previous, stalls = place(b, 'B', y, 'Y', previous, first, stalls, i)
        elif r >= b >= y:
            r, b, previous, stalls = place(r, 'R', b, 'B', previous, first, stalls, i)
        elif r >= y >= b:
            r, y, previous, stalls = place(r, 'R', y, 'Y', previous, first, stalls, i)
        elif y >= b >= r:
            y, b, previous, stalls = place(y, 'Y', b, 'B', previous, first, stalls, i)
        elif y >= r >= b:
            y, r, previous, stalls = place(y, 'Y', r, 'R', previous, first, stalls, i)
        else:
            raise Exception()

    return ''.join(stalls) + remainder

    # colors = sorted([(b, 'B'), (r, 'R'), (y, 'Y')], key=lambda x: x[0], reverse=True)
    # stalls = [None for __ in xrange(int(n))]
    # for nc, color in colors:
    #     if nc == 0:
    #         continue
    #     d = int(n/nc)
    #     for i in xrange(nc):
    #         stalls[i] = d*nc


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as h:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            n, r, o, y, g, b, v = map(int, f.readline().strip().split())
            soln = smallsolve(n, r, y, b)

            if soln[0] == soln[-1] or 'RR' in soln or 'BB' in soln or 'YY' in soln:
                print i
                print r, y, b
                print soln
                raise Exception()

            if soln != 'IMPOSSIBLE':
                if soln.count('R') != r:
                    print n, r, y, b, soln
                    raise Exception()
                if soln.count('Y') != y:
                    print n, r, y, b, soln
                    raise Exception()
                if soln.count('B') != b:
                    print n, r, y, b, soln
                    raise Exception()

            outline = 'Case #{i}: {soln}\n'.format(**locals())
            h.write(outline)
            print outline,


if __name__ == '__main__':
    main()
