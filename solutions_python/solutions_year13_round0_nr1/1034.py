#!/usr/bin/env python2
# by Santiago Saavedra

T = 'T'

class Graph(object):
    def __init__(self, alist):
        self.alist = alist

    def get(self, i, j):
        return self.alist[i][j]

    def get_connection(self, i, j, visited=set()):
        visited.add((i, j))
        char = self.get(i, j)

        positions = [ (x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) if x != i and y != j and x > 0 and y > 0 and x < 4 and y < 4 and (x,y) not in visited ]

        r = [(i, j)]
        for i, j in positions:
            r.append(self.get_connection(i, j, visited))
        return r

        return positions


def check_diagonal(case, letters):
    num = 0
    # print case, 'detecting', letters
    for i in range(4):
        if case[i][i] in letters:
            num += 1
            # print 'Yay', i, i
        else:
            # print 'Ooh', i, i, case[i][i]
            break
    return num == 4

def solve_game(letters, case, msg=True):
    # print '-- Now solving ', case, ' for ', letters, ' --'
    for line in case:
        if len(filter(lambda x: x in letters, line)) == 4:
            return msg

    # Diagonal
    if check_diagonal(case, letters):
        return msg
    
    # print 'before:', case
    case = zip(*case[::-1])
    # print 'after:', case
    for line in case:
        if len(filter(lambda x: x in letters, line)) == 4:
            return msg
    if check_diagonal(case, letters):
        return msg
    return None

def solve_for_x(case):
    return solve_game('XT', case, 'X won')

def solve_for_o(case):
    return solve_game('OT', case, 'O won')

def parse_case(case):
    visited = set()

    casej = "".join(case)
    if(len(filter(lambda x: x == 'X', casej)) > len(filter(lambda x: x == 'O', casej))):
        first, second = solve_for_x, solve_for_o
    else:
        first, second = solve_for_o, solve_for_x

    a = first(case)
    if a:
        return a
    b = second(case)
    if b:
        return b

    if '.' in casej:
        return 'Game has not completed'
    return 'Draw'
    g = Graph(case)
    return g.get_connection(0, 0, visited)


def parse_input(lines):
    num = int(lines[0])
    lines = lines[1:]
    cases = []
    for i in range(num):
        cases.append(lines[5*i:5*i+4])

    return cases



def main():
    import sys
    cases = parse_input(map(lambda a: a.replace("\n", ''), sys.stdin.readlines()))
    for i, case in enumerate(cases, start=1):
        print "Case #%d: %s" % (i, parse_case(case))

if __name__ == '__main__':
    main()




