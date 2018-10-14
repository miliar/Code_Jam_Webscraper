import sys
import functools

def read_case(line):
    splited = line.split()
    n = int(splited[0])
    splited = splited[1:]
    moves = [(splited[2*i], int(splited[2*i + 1])) for i in xrange(n)]
    return moves


def read_input(path):
    cases = []
    with file(path) as f:
        lines = iter(f)
        n = int(lines.next())

        for i in range(1, 1 + n):
            cases.append((i, read_case(lines.next())))

    return cases

def next(moves, robot):
    for who, button in moves:
        if who == robot:
            return button

    return None

next_blue = functools.partial(next, robot='B')
next_orange = functools.partial(next, robot='O')

def next_robot(moves):
    return moves[0][0]

def move_once(pos, next_pos):
    if next_pos > pos:
        return pos + 1
    if next_pos < pos:
        return pos - 1
    return pos

def solve(moves):
    blue = orange = 1

    t = 0
    while moves:
        next_blue_move = next_blue(moves)
        next_orange_move = next_orange(moves)
        next_to_push = next_robot(moves)

        if next_to_push == 'O':
            while orange != next_orange_move:
                orange = move_once(orange, next_orange_move)
                blue = move_once(blue, next_blue_move)
                t += 1

            t += 1 # actually pushing
            blue = move_once(blue, next_blue_move)
        else:
            while blue != next_blue_move:
                orange = move_once(orange, next_orange_move)
                blue = move_once(blue, next_blue_move)
                t += 1

            t += 1 # actually pushing
            orange = move_once(orange, next_orange_move)

        
        moves.pop(0)
        

    return t
    
    
    
    


if __name__ == '__main__':
    cases = read_input(sys.argv[1])
    for i, case in cases:
        print 'Case #%d: %d' % (i, solve(case))
