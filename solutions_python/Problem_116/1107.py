#!/usr/bin/env python3
import sys


def test_won(data, p):
    for i in range(4):
        if all(data[i][j] in [p, 'T'] for j in range(4)):
            return True

    for j in range(4):
        if all(data[i][j] in [p, 'T'] for i in range(4)):
            return True

    if all(data[i][i] in [p, 'T'] for i in range(4)):
        return True

    if all(data[i][4 - i - 1] in [p, 'T'] for i in range(4)):
        return True

    return False


def solve(data):
    if test_won(data, 'X'):
        return 'X won'
    if test_won(data, 'O'):
        return 'O won'
    if ''.join(data).find('.') == -1:
        return 'Draw'
    return 'Game has not completed'


def read(fin):
    r = []
    for i in range(4):
        r.append(fin.readline().rstrip())
    fin.readline()
    return r


def main():
    try:
        fin = open(sys.argv[1])
        if len(sys.argv) >= 3:
            fout = open(sys.argv[2], 'w')
        else:
            fout = sys.stdout
    except IndexError:
        print('Not enough command line options')
        sys.exit(1)
    except IOError as e:
        print(e)
        sys.exit(2)

    T = int(fin.readline())
    for t in range(T):
        data = read(fin)
        print('Case #{}: {}'.format(t + 1, solve(data)), file=fout)


if __name__ == '__main__':
    main()
