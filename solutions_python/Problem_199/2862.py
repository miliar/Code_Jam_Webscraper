import sys


def invert(l):
    return ['+' if x == '-' else '-' for x in l]


def solve_case(line):
    cakeline, flip = line.split()
    flip = int(flip)
    stack = list(cakeline)
    flipcount = 0
    while len(stack) > flip:
        cake = stack.pop()
        if cake == '-':
            flipcount += 1
            stack.append(cake)
            stack[-flip:] = invert(stack[-flip:])
    minuscount = stack.count('-')
    if minuscount == 0:
        result = str(flipcount)
    elif minuscount == flip:
        result = str(flipcount + 1)
    else:
        result = 'IMPOSSIBLE'
    return result


def solve(inp, out):
    inp.readline()
    for i, line in enumerate(inp):
        if line.strip():
            result = solve_case(line.strip())
            out.write('Case #%d: %s\n' % (i+1, result))


if __name__ == '__main__':
    solve(sys.stdin, sys.stdout)
