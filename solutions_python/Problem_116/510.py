

def check(a, s):
    def v(c):
        return c == s or c == 'T'
    return any(all(v(a[i][j]) for j in range(4)) for i in range(4)) or \
           any(all(v(a[j][i]) for j in range(4)) for i in range(4)) or \
           all(v(a[i][i]) for i in range(4)) or \
           all(v(a[i][3-i]) for i in range(4))

def tttt(a):
    if check(a, 'X'):
        return 'X'
    elif check(a, 'O'):
        return 'O'
    if any('.' in row for row in a):
        return -2
    else:
        return -1

def case(file):
    a = []
    for i in range(4):
        a.append(list(file.readline().strip()))
    file.readline()
    b = tttt(a)
    if b == -1:
        return "Draw"
    elif b == -2:
        return "Game has not completed"
    else:
        return "%s won" % b


def cases(in_name, func=None, out_name=None):
    if func is None:
        func = case
    if out_name is None:
        ext = in_name.rindex('.')
        out_name = in_name[:ext] + ".out"
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            ntests = int(fin.readline())
            for i in range(1, ntests + 1):
                fout.write("Case #%i: %s\n" % (i, func(fin)))

cases("A-large.in")