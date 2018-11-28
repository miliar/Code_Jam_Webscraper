#!/usr/bin/env python2


def main():
    outs = []
    # read and parse input

    with open('input.in', 'r') as inp:
        test_cases_number = int(inp.readline())

        for i in range(test_cases_number):
            row1 = row2 = None

            # take the n-th row (where n is the card chosen by the volunteer
            c = int(inp.readline())
            for j in range(4):
                if j == c-1:
                    row1 = map(int, inp.readline().split(' '))
                else:
                    inp.readline()

            # same as above, but for the second arrangement
            c = int(inp.readline())
            for j in range(4):
                if j == c-1:
                    row2 = map(int, inp.readline().split(' '))
                else:
                    inp.readline()

            # the card is the common element of the two rows
            out = 'Case #{0}: '.format(i+1)
            intersection = filter(lambda x: x in row2, row1)

            if not intersection:
                out += 'Volunteer cheated!'
            elif len(intersection) > 1:
                out += 'Bad magician!'
            else:
                out += str(intersection[0])
            outs.append(out)

    with open('output.out', 'w') as output:
        output.write('\n'.join(outs))

if __name__ == '__main__':
    main()
