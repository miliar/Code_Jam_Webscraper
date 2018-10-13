import sys

def read_case(l):
    au = l.strip().split()[1]
    return [int(x) for x in au]

def cant(c):
    inv = [i - sum(c[:i]) for i in range(len(c))]
    return max(0, max(inv))

def rint():
    return int(rline())

def rline():
    global linenr
    linenr += 1
    return stdin[linenr - 1]

global stdin
global linenr
stdin = sys.stdin.readlines()
linenr = 0
cases = rint()
case = 1
while linenr < len(stdin):
    c = read_case(rline())
    print 'Case #{0}: {1}'.format(case, cant(c))
    case += 1


