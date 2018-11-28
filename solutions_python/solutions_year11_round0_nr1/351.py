import itertools
import operator

def parse_line(line):
    fields = line.split()[1:]
    return [(robot, int(button)) for robot, button in zip(fields[::2], fields[1::2])]

def iter_moves(seq):
    pos = {'O': 1, 'B': 1}
    for robot, button in seq:
        yield robot, abs(pos[robot] - button) + 1
        pos[robot] = button

def solve(seq):
    result = 0
    prev = 0
    for _, move_grp in itertools.groupby(iter_moves(seq), key=operator.itemgetter(0)):
        for i, (robot, n) in enumerate(move_grp):
            if i == 0:
                this_move = max(n-1-prev, 0) + 1
                prev = 0
            else:
                this_move = n
            prev += this_move
            result += this_move
    return result

if __name__ == '__main__':
    import sys
    for i, line in enumerate(itertools.islice(sys.stdin, 1, None), 1):
        print 'Case #{}: {}'.format(i, solve(parse_line(line)))
