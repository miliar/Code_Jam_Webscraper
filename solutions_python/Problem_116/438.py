import sys
sys.setrecursionlimit(10000)


def read_ints():
    a = raw_input().split()
    return [int(x) for x in a]


def read_int():
    return read_ints()[0]

pos = []
pos += [[(x, y) for x in range(0, 4)] for y in range(0, 4)]
pos += [[(y, x) for x in range(0, 4)] for y in range(0, 4)]
pos += [[(x, x) for x in range(0, 4)]]
pos += [[(x, 3-x) for x in range(0, 4)]]


def count(seq, player='O'):
    return sum(map(lambda x: x == player or x == 'T', seq))


def getseq(table, pos):
    return [table[y][x] for x, y in pos]


def solve():
    # .. won
    # Draw
    # Game has not completed
    table = [raw_input() for x in range(5)]
    for p in pos:
        seq = getseq(table, p)
        for winner in ['O', 'X']:
            if count(seq, winner) == 4:
                return '%s won' % winner

    if any(table[y][x] == '.' for y in range(4) for x in range(4)):
        return 'Game has not completed'
    return 'Draw'


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())
