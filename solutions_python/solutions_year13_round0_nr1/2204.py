#!/usr/bin/python

def check(line, state):
    (x_won, o_won, not_completed, lines) = state
    if x_won:
        return state
    if o_won:
        return state
    if line == "TXXX" or line == "XTXX" or line == "XXTX" or line == "XXXT":
        return (True, o_won, not_completed, lines)
    if line == "TOOO" or line == "OTOO" or line == "OOTO" or line == "OOOT":
        return (x_won, True, not_completed, lines)
    if line == "XXXX":
        return (True, o_won, not_completed, lines)
    if line == "OOOO":
        return (x_won, True, not_completed, lines)
    if line[0] == "." or line[1] == "." or line[2] == "." or line[3] == ".":
        return (x_won, o_won, True, lines)
    return state

def solve(line, num, state):
    (x_won, o_won, not_completed, lines) = state
    if num == 4:
        for i in range(6):
            state = check(lines[i], state)
    else:
        state = check(line, state)
        (x_won, o_won, not_completed, lines) = state
        for i in range(4):
            lines[i] += line[i]
        lines[4] += line[num]
        lines[5] += line[3 - num]
        state = (x_won, o_won, not_completed, lines)
    return state

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    [N] = readints(inp)

    for n in range(N):
        x_won = False
        o_won = False
        not_completed = False
        lines = []
        for i in range(6):
            lines.append(str())
        state = (x_won, o_won, not_completed, lines)
        for j in range(5):
            state = solve(inp.readline().strip(), j, state)
        (x_won, o_won, not_completed, lines) = state
        if x_won:
            result = 'X won'
        elif o_won:
            result = 'O won'
        elif not_completed:
            result = 'Game has not completed'
        else:
            result = 'Draw'
        print 'Case #%s: %s' % ((n+1), result)
