import sys

"""
def solve(x, s):
    #bigs = s*x
    xl = len(s)*x
    if len(s)*x < 3:
        return "NO"

    r = red(s)
    middle = [(1, '1'), r]
    while middle[-1] != middle[0]:
        middle.append(mult(middle[-1], r))
    middle.pop()

    beg = [(1, '1')]
    for l in s:
        beg.append(mult(beg[-1], (1, l)))
    end = [(1, '1')]
    for l in reversed(s):
        end.append(mult((1, l), end[-1]))
    pr = (beg, middle, end)

    for i in range(1, xl-1):
        #assert redcut(s, 0, i, pr) == red(bigs[0:i]), ", ".join([str(x) for x in [s, x, i]])
        if good(redcut(s, 0, i, pr), 'i'):
            for j in range(i, xl):
                #assert redcut(s, i, j, pr) == red(bigs[i:j])
                #assert redcut(s, j, xl, pr) == red(bigs[j:xl])
                if good(redcut(s, i, j, pr), 'j') and good(redcut(s, j, xl, pr), 'k'):
                    return "YES"
    return "NO"
"""

def d(*args):
    sys.stderr.write(', '.join(map(str, args)) + "\n")

def printf(*args):
    print(''.join(map(str, args)))

def int_input():
    return list(map(int, input().split(' ')))

mul = {
    '11': (1, '1'),
    '1i': (1, 'i'),
    '1j': (1, 'j'),
    '1k': (1, 'k'),

    'i1': (1, 'i'),
    'ii': (-1, '1'),
    'ij': (1, 'k'),
    'ik': (-1, 'j'),

    'j1': (1, 'j'),
    'ji': (-1, 'k'),
    'jj': (-1, '1'),
    'jk': (1, 'i'),

    'k1': (1, 'k'),
    'ki': (1, 'j'),
    'kj': (-1, 'i'),
    'kk': (-1, '1')
}

def mult(a, b):
    r = mul[a[1] + b[1]]
    return (r[0]*a[0]*b[0], r[1])

def red(s):
    k = (1, '1')
    for l in s:
        k = mult(k, (1, l))
    return k

def good(r, l):
    return r[0] == 1 and r[1] == l

def inv(r):
    return (r[0] if r[1] == '1' else -r[0], r[1])

def redcut(s, i, j, pr):
    iq, ir = divmod(i, len(s))
    jq, jr = divmod(j, len(s))
    if iq == jq:
        #return red(s[ir:jr])
        return mult(inv(pr[0][ir]), mult(pr[1][1%len(pr[1])], inv(pr[2][len(s)-jr])))
    else:
        #beg = red(s[ir:])
        beg = pr[2][len(s)-ir]
        middle = pr[1][(jq-iq-1)%len(pr[1])]
        #end = red(s[:jr])
        end = pr[0][jr]
        return mult(beg, mult(middle, end))

def solve(x, s):
    xl = len(s)*x
    if len(s)*x < 3:
        return "NO"

    r = red(s)
    middle = [(1, '1'), r]
    while middle[-1] != middle[0]:
        middle.append(mult(middle[-1], r))
    middle.pop()

    beg = [(1, '1')]
    for l in s:
        beg.append(mult(beg[-1], (1, l)))
    end = [(1, '1')]
    for l in reversed(s):
        end.append(mult((1, l), end[-1]))
    pr = (beg, middle, end)

    gi = []
    r = (1, '1')
    for i in range(xl):
        if good(r, 'i'):
            gi.append(i)
        r = mult(r, (1, s[i%len(s)]))

    gk = []
    r = (1, '1')
    for i in range(xl-1, -1, -1):
        r = mult((1, s[i%len(s)]), r)
        if good(r, 'k'):
            gk.append(i)
    for k in gk:
        assert good(redcut(s, k, xl, pr), 'k')

    for i in gi:
        for k in gk:
            if k > i and good(redcut(s, i, k, pr), 'j'):
                return "YES"
    #for i in range(1, xl-1):
        #if good(redcut(s, 0, i, pr), 'i'):
            #for j in range(i, xl):
                #if good(redcut(s, i, j, pr), 'j') and good(redcut(s, j, xl, pr), 'k'):
                    #return "YES"
    return "NO"

def read_input():
    (l, x) = tuple(int_input())
    return x, input()


if __name__ == '__main__':
    for i in range(int(input())):
        printf("Case #", i+1, ": ", (solve(*read_input())))
