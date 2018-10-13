import sys

def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())

def test(lines, symbol):
    ss = [symbol, 'T']
    for i in range(4):
        for j in range(4):
            if lines[i][j] not in ss:
                break
        else:
            return True
        for j in range(4):
            if lines[j][i] not in ss:
                break
        else:
            return True
    for i in range(4):
        if lines[i][i] not in ss:
            break
    else:
        return True
    for i in range(4):
        if lines[i][3 - i] not in ss:
            break
    else:
        return True

def solve():
    lines = [raw_input() for i in range(4)]
    if test(lines, 'X'):
        return 'X won'
    if test(lines, 'O'):
        return 'O won'
    if '.' in ''.join(lines):
        return 'Game has not completed'
    return 'Draw'

case_number = readint()
for case in xrange(case_number):
    print "Case #%s: %s" % (case + 1, solve())
    raw_input()
