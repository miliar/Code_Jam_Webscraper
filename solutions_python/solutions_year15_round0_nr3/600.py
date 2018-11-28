import sys
input = sys.stdin.readline

_table = [
    [0, 1, 2, 3],
    [1, 4, 3, 6],
    [2, 7, 4, 1],
    [3, 2, 5, 4],
]

def mul(a, b):
    return _table[a&3][b&3] ^ (a&4) ^ (b&4)

def check(s):
    z = 0
    c = []
    for i in reversed(s):
        z = mul(i, z)
        c.append(z)
    c.reverse()

    qi = 0
    l = len(s)
    for i in xrange(l-2):
        qi = mul(qi, s[i])
        if qi == 1:
            qj = 0
            for j in xrange(i+1, l-1):
                qj = mul(qj, s[j])
                if qj == 2:
                    if c[j+1] == 3:
                        return True
    return False


for _ in xrange(int(input())):
    l, x = map(int, input().split())
    s = [ord(i) - 104 for i in input().rstrip()] * x
    print 'Case #%d: %s' % (_+1, ['NO', 'YES'][check(s)])