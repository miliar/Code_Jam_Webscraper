import argparse
import sys


class Board(object):
    def __init__(self, data):
        self.data = data

    def test(self, values):
        if '.' not in values:
            if len(values) == 1:
                return values.pop()
            elif len(values) == 2 and 'T' in values:
                v = values.pop()
                if v == 'T':
                    v = values.pop()
                return v

        return None

    def solve(self):
        # check for rows
        for r in range(0, 4):
            v = self.test(set(self.data[r]))
            if v != None:
                return '%s won' % v

        # check columns
        for c in range(0, 4):
            v = self.test(set([self.data[r][c] for r in range(0, 4)]))
            if v != None:
                return '%s won' % v

        # check diagonals
        v = self.test(set([self.data[i][i] for i in range(0, 4)]))
        if v != None:
            return '%s won' % v
        v = self.test(set([self.data[-(i+1)][i] for i in range(0, 4)]))
        if v != None:
            return '%s won' % v

        # check for incomplete game
        for d in self.data:
            if '.' in d:
                return 'Game has not completed'

        return 'Draw'

def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--learn', action='store_true', default=False)
    parser.add_argument('--solve', action='store_true', default=False)
    parser.add_argument('files', nargs=1)
    arguments = parser.parse_args(args)

    with open(arguments.files[0], 'r') as f:
        n = int(f.readline())
        for i in range(0, n):
            definition = []
            for j in range(0, 4):
                definition.append(f.readline().strip())
            f.readline()

            board = Board(definition)
            print 'Case #%d: %s' % (i+1, board.solve(),)

if __name__ == '__main__':
    sys.exit(main())
