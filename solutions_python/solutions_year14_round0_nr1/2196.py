import sys

def main(lines):

    ncases = int(lines.pop(0))

    for case in xrange(ncases):

        txt = ''

        ans1 = lines.pop(0)
        row1 = ''

        for i in xrange(4):
            if i == int(ans1) - 1:
                row1 = lines.pop(0)

            else:
                lines.pop(0)

        ans2 = lines.pop(0)
        row2 = ''

        for i in xrange(4):
            if i == int(ans2) - 1:
                row2 = lines.pop(0)

            else:
                lines.pop(0)

        result = set(row2.split()) & set(row1.split())
        if not result:
            txt = 'Volunteer cheated!'

        elif len(result) == 1:
            txt = result.pop()

        else:
            txt = 'Bad magician!'
        
        print 'Case #%d: %s' % (case + 1, txt)


if __name__ == '__main__':
    main(sys.stdin.readlines())
