# DISCLAIMER
# This is by far the ugliest code I've written in a Looong while. I should have
# called a day. Instead, I stubbornly and mindlessly carried on.
from sys import stdin, stdout, stderr
from collections import deque

MAP = {
    "1": {
        "1": "1",
        "i": "i",
        "j": "j",
        "k": "k"
    },
    "i": {
        "1": "i",
        "i": "-1",
        "j": "k",
        "k": "-j"
    },
    "j": {
        "1": "j",
        "i": "-k",
        "j": "-1",
        "k": "i"
    },
    "k": {
        "1": "k",
        "i": "j",
        "j": "-i",
        "k": "-1"
    },
}

def de_neg(n):
    if n.startswith('-'):
        return (1, n[1:])
    return (0, n)

def rem_repeated(d):
    if len(d) > 4 and d[0] == d[1] == d[2] == d[3] == d[4]:
        d.popleft()
        d.popleft()
        d.popleft()
        d.popleft()
        return True
    if len(d) > 3 and d[0] == d[1] == d[2] == d[3]:
        d.popleft()
        d.popleft()
        d.popleft()
        d.popleft()
        d.extendleft('1')
        return True
    # if len(d) > 2 and d[0] == d[1] == d[2]:
    #     d.popleft()
    #     d.popleft()
    #     e = d.popleft()
    #     d.extendleft('-' + e)
    #     return True

    # if len(d) > 1 and d[0] == d[1]:
    #     d.popleft()
    #     d.popleft()
    #     d.extendleft('-1')
    #     return True

    return False

def lookup(i, j):
    r = MAP[i][j]
    if r.startswith("-"):
        return (1, r[1])
    return (0, r)

def to_str(t):
    return "{0}{1}".format("" if t[0] == 0 else "-", t[1])

def to_exp(n):
    if n.startswith('-'):
        return (1, n[1:])
    return (0, n)

def simplify(s, mem={}):
    if s in mem:
        return mem[s]
    else:
        if s.startswith("-"):
            d = deque(s[1:])
            neg = 1
        else:
            d = deque(s)
            neg = 0
        while len(d) > 1:

            while rem_repeated(d):
                tup = de_neg(d[0])
                neg += tup[0]
                d[0] = tup[1]

            if len(d) == 1:
                break;
            a, b = d[0], d[1]
            tup = de_neg(MAP[a][b])
            neg += tup[0]
            d.popleft()
            d.popleft()
            d.extendleft(tup[1])

        r = ("" if neg % 2 == 0 else "-") + d[0]
        mem[s] = r
        return r

def simple(s):
    if s.startswith("-"):
        d = deque(s[1:])
        neg = 1
    else:
        d = deque(s)
        neg = 0
    while len(d) > 1:

        while rem_repeated(d):
            pass

        if len(d) == 1:
            break;
        a, b = d[0], d[1]
        tup = de_neg(MAP[a][b])
        neg += tup[0]
        d.popleft()
        d.popleft()
        d.extendleft(tup[1])

    return ((neg % 2), d[0])


def impossible(s, target):
    alt = [k for k in MAP[target].keys() if k not in (target, "1")]
    possible = target in s or (alt[0] in s and alt[1] in s)
    return not possible


def solve(x, s, c):
    mem = {}
    def rev_simplify(s):
        if s in mem:
            return mem[s]

        l = len(s)

        if l < 10:
            r = simple(s)
            mem[s] = r
            return r

        if l == 1:
            return (0, s)

        if s.startswith("-"):
            sub = rev_simplify(s[1:])
            r = ((1 + sub[0]) % 2, sub[1])
            mem[s] = r
            return r

        if l == 2:
            r = lookup(s[0], s[1])
            mem[s] = r
            return r

        i = l / 2
        s1 = rev_simplify(s[:i])
        s2 = rev_simplify(s[i:])
        comb = lookup(s1[1], s2[1])

        r = ((s1[0] + s2[0] + comb[0]) % 2, comb[1])
        mem[s] = r
        return r

    s = x * s
    i_prev = ""

    for i in range(0, len(s) - 2):
        s1 = i_prev + s[i]
        i_prev = to_str(rev_simplify(s1))
        # i_prev = simplify(s1)
        if i_prev == "i":
            j_prev = ""
            for j in range(i + 1, len(s) - 1):
                s2 = j_prev + s[j]
                # j_prev = to_str(rev_simplify(s2))
                j_prev = simplify(s2)
                if j_prev == "j":
                    s3 = s[j+1:]
                    k_prev = to_str(rev_simplify(s3))
                    return k_prev == "k"


if __name__ == "__main__":

    cases = int(stdin.readline())
    for c in xrange(1, cases + 1):
        l, x = [int(i) for i in stdin.readline().split()]
        s = stdin.readline().strip()
        ans = solve(x, s, c)
        stdout.write("Case #{0}: {1}\n".format(c, "YES" if ans else "NO"))
        stderr.write("Case #{0}: {1}\n".format(c, "YES" if ans else "NO"))
