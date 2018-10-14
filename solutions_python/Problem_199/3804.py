from __future__ import print_function
import sys

f = open('A-large.in', 'r')
outfile = open('A-large.out', 'w')

def debug(str):
    print(str, file=sys.stderr)

def output(case, flips):
    print("Case #{0}: {1}".format(case, flips), file=outfile)
    debug("Case #{0}: {1}".format(case, flips))

def flip_point(stack):
    debug("flip point")
    debug('"' + stack + '"')
    pos = stack.find('-')
    if pos < 0:
        return None
    return pos

swap = {}
swap['+'] = '-'
swap['-'] = '+'
def flip(stack, i, k):
    debug('flip: {0} pos {1} length {2}'.format(stack, i, k))
    stack = stack[:i] + ''.join(map(lambda x: swap[x], stack[i:i+k])) + stack[i+k:]
    debug('flip result: {0}'.format(stack))
    return stack

f.readline()
case = 1
for line in f.readlines():
    parts = line.split(' ')
    stack = parts[0]
    k = int(parts[1])
    i = 0

    point = flip_point(stack)
    if point == None:
        output(case, i)
    elif point + k > len(stack):
        debug('too far')
        point = None
        output(case, 'IMPOSSIBLE')
        case += 1
        continue

    while point != None:
        stack = flip(stack, point, k)
        point = flip_point(stack)
        i += 1
        if point == None:
            output(case, i)
            break
        elif point + k > len(stack):
            debug('too far')
            point = None
            output(case, 'IMPOSSIBLE')
    case += 1