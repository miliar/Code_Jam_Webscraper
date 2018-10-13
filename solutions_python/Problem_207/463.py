allowed = dict(r={'y', 'g', 'b'},
               o={'b'},
               y={'b', 'v', 'r'},
               g={'r'},
               b={'r', 'o', 'y'},
               v={'y'},
               )


def sequence(n, r, o, y, g, b, v):
    a = []
    while n:
        # print a
        if not len(a):
            if r:
                a.append('R')
                r -= 1
                n -= 1
            elif o:
                a.append('O')
                o -= 1
                n -= 1
            elif y:
                a.append('Y')
                y -= 1
                n -= 1
            elif g:
                a.append('G')
                g -= 1
                n -= 1
            elif b:
                a.append('B')
                b -= 1
                n -= 1
            elif v:
                a.append('V')
                v -= 1
                n -= 1
        else:

            if a[-1] == 'G':
                if r:
                    a.append('R')
                    r -= 1
                    n -= 1
                else:
                    return 'IMPOSSIBLE'

            elif a[-1] == 'O':
                if b:
                    a.append('B')
                    b -= 1
                    n -= 1
                else:
                    return 'IMPOSSIBLE'

            elif a[-1] == 'V':
                if y:
                    a.append('Y')
                    y -= 1
                    n -= 1
                else:
                    return 'IMPOSSIBLE'

            elif a[-1] == 'R':
                if g:
                    a.append('G')
                    g -= 1
                    n -= 1
                elif y > b or (y and y == b and a[0] == 'Y'):
                    a.append('Y')
                    y -= 1
                    n -= 1
                elif b:
                    a.append('B')
                    b -= 1
                    n -= 1
                else:
                    return 'IMPOSSIBLE'

            elif a[-1] == 'Y':
                if v:
                    a.append('V')
                    v -= 1
                    n -= 1
                elif b > r or (b and b == r and a[0] == 'B'):
                    a.append('B')
                    b -= 1
                    n -= 1
                elif r:
                    a.append('R')
                    r -= 1
                    n -= 1
                else:
                    return 'IMPOSSIBLE'

            elif a[-1] == 'B':
                if o:
                    a.append('O')
                    o -= 1
                    n -= 1
                elif r > y or (r and r == y and a[0] == 'R'):
                    a.append('R')
                    r -= 1
                    n -= 1
                elif y:
                    a.append('Y')
                    y -= 1
                    n -= 1
                else:
                    return 'IMPOSSIBLE'

    if a[-1] == 'R' and a[0] not in ('Y', 'G', 'B'):
        return 'IMPOSSIBLE'
    if a[-1] == 'O' and a[0] != 'B':
        return 'IMPOSSIBLE'
    if a[-1] == 'Y' and a[0] not in ('B', 'V', 'R'):
        return 'IMPOSSIBLE'
    if a[-1] == 'G' and a[0] != 'R':
        return 'IMPOSSIBLE'
    if a[-1] == 'B' and a[0] not in ('R', 'O', 'Y'):
        return 'IMPOSSIBLE'
    if a[-1] == 'V' and a[0] != 'Y':
        return 'IMPOSSIBLE'
    return ''.join(a)


def process(filename):
    answers = []
    with open(filename + '.in') as f:
        lines = tuple(f.readlines())
    cases = int(lines[0])
    for x in range(1, cases + 1):
        n, r, o, y, g, b, v = map(int, lines[x].split())
        answers.append('Case #{}: {}'.format(x, sequence(n, r, o, y, g, b, v)))
    with open(filename + '.out', 'w') as f:
        f.write('\n'.join(answers))


if __name__ == '__main__':
    process('B-sample')
    process('B-small-attempt2')
    # process('B-large')
