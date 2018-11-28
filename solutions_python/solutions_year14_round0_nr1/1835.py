def parse_file(fnIn, fnOut):
    with open(fnOut, 'w') as fOut:
        with open(fnIn, 'rU') as fIn:
            T = int(fIn.readline())

            for n in xrange(T):
                q1 = read_question(fIn)
                q2 = read_question(fIn)

                result = do_magic(q1, q2)

                fOut.write('Case #%d: %s\n'%(n + 1, result))


def read_question(f):
    ans = int(f.readline())

    cards = [map(int, f.readline().split()) for _ in xrange(4)]

    return ans - 1, cards


def do_magic(q1, q2):
    q1ans,q1cards = q1
    q2ans,q2cards = q2

    possible = set(q1cards[q1ans]).intersection(q2cards[q2ans])
    lp = len(possible)

    if lp == 0:
        return 'Volunteer cheated!'
    elif lp == 1:
        return possible.pop()
    else:
        return 'Bad magician!'
