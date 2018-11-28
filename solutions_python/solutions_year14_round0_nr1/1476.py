import sys


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        first_guess = int(stdin.readline())
        for r in range(1, 5):
            line = stdin.readline()
            if r == first_guess:
                row = map(int, line.split())

        second_guess = int(stdin.readline())
        for r in range(1, 5):
            line = stdin.readline()
            if r == second_guess:
                row2 = map(int, line.split())

        intersection = set(row) & set(row2)

        if len(intersection) > 1:
            print "Case #%d: Bad magician!" % (i+1)
        elif len(intersection) < 1:
            print "Case #%d: Volunteer cheated!" % (i+1)
        else:
            elem = intersection.pop()
            print "Case #%d: %d" % (i+1, elem)
