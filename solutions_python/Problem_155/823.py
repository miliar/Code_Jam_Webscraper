import sys

from utils import stripped_lines


def solve(counts):
    invitations = 0
    clapping = 0
    for shyness, count in enumerate(counts):
        if shyness > clapping:
            new_invitations = shyness - clapping
            invitations += new_invitations
            clapping += new_invitations
        clapping += count
    return invitations


def main():
    lines = stripped_lines(sys.stdin)
    numcases = int(lines.next())

    for i in range(numcases):
        line = lines.next()
        counts = [int(c) for c in line.split()[-1]]

        result = solve(counts)

        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
