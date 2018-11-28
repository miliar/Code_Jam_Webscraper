from sys import stdin


def main():
    cases = int(stdin.readline())
    for t in range(cases):
        a1 = int(stdin.readline())
        for i in range(4):
            line = stdin.readline()
            if i + 1 == a1:
                row1 = set(line.split())

        a2 = int(stdin.readline())
        for i in range(4):
            line = stdin.readline()
            if i + 1 == a2:
                row2 = set(line.split())

        ans = list(row1.intersection(row2))
        print 'Case #%d:' % (t + 1),
        if len(ans) == 1:
            print ans[0]
        elif len(ans) == 0:
            print 'Volunteer cheated!'
        else:
            print 'Bad magician!'


if __name__ == '__main__':
    main()
