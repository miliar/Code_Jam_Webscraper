#!/usr/bin/python3

def main():
    T = int(input())

    for i in range(T):
        rows = list()

        for _ in range(2):
            rowno = int(input())
            for r in range(4):
                row = [int(x) for x in input().split()]
                if r+1 == rowno:
                    rows.append(row)

        xsect = set(rows[0]).intersection(set(rows[1]))

        if len(xsect) == 0:
            result = 'Volunteer cheated!'
        elif len(xsect) == 1:
            result = xsect.pop()
        else:
            result = 'Bad magician!'

        print('Case #{0}: {1}'.format(i+1, result))

if __name__ == '__main__':
    main()
