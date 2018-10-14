from __future__ import print_function
from sys import stderr

def eprint(*args):
    print(*args, file=stderr)

def makeAnswer(i, answers):
    return ('Case #%d: ' % (i+1)) + '\n'.join(answers)

cmap = {
    'R':1,
    'Y':2,
    'B':4,
    'O':3,
    'G':6,
    'V':5
}

carr = ['?', 'R', 'Y', 'O', 'B', 'V', 'G']

def solve(i):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split()]
    multiArr = [[cmap['O']]*o] + [[cmap['G']]*g] + [[cmap['V']]*v]
    singleArr = [[cmap['R']]*r] + [[cmap['Y']]*y] + [[cmap['B']]*b]
    lastColor = 0
    answer = []
    while len(answer) < n:
        multiArr.sort(lambda x, y: 0 if len(x) == len(y) else 1 if len(x) < len(y) else -1)
        color = [c for c in multiArr if len(c) != 0 and lastColor & c[0] == 0]
        if len(color) > 0:
            lastColor = color[0][0]
            del color[0][0]
            answer.append(lastColor)
            continue

        singleArr.sort(lambda x, y: 0 if len(x) == len(y) else 1 if len(x) < len(y) else -1)
        color = [c for c in singleArr if len(c) != 0 and lastColor & c[0] == 0]
        if len(color) > 0:
            lastColor = color[0][0]
            del color[0][0]
            answer.append(lastColor)
            continue

        return ['IMPOSSIBLE']

    if answer[0] & answer[-1] != 0:
        answer[-1], answer[-3] = answer[-3], answer[-1]

    if answer[0] & answer[-1] != 0:
        return ['IMPOSSIBLE']

    return [''.join(carr[c] for c in answer)]

if __name__ == '__main__':
    numCases = int(raw_input())

    # calculate
    solutions = (solve(i) for i in xrange(numCases))

    # print
    print('\n'.join((makeAnswer(i, solution) for i, solution in enumerate(solutions))))
