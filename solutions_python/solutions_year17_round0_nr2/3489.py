# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

input = """4
132
1000
7
111111111111111110
"""

output = """
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999
"""

def untidy(n):
    for i, dig in enumerate(n):
        if i == 0:
            continue
        if dig < n[i - 1]:
            return i
    else:
        return None

def solve_one(n):
    pos_broken = untidy(n)

    nlist = map(int, list(n))
    """
    0123456789 len=10
          v--- broken
    1234563777
    1234559999
        -1

          v--- broken
    11111101234
         v--- broken
    999990 -> 999989 - wrong, do many attempts
    """
    print n, pos_broken
    if n[pos_broken - 1] == '1':
        return '9' * (len(n) - 1)

    nlist[pos_broken - 1] -= 1
    for i in xrange(pos_broken, len(n)):
        nlist[i] = 9
    return ''.join(map(str, nlist))

def solve(n):
    while untidy(n):
        n = solve_one(n)
    return n


def get_input(lines):
    out = []
    for i in xrange(1, len(lines)):
        print "line %s / %s" % (i, len(lines) - 1)
        if not lines[i]:
            continue
        x = lines[i].strip()
        res = solve(x)
        out.append("Case #%s: %s\n" % (i, res))
    return out


fin_name = "B-large.in"
fout_name = fin_name + ".out"
with open(fin_name) as fin:
    with open(fout_name, "w") as fout:
        fout.writelines(get_input(fin.readlines()))
        print "done, written to %s" % fout_name
