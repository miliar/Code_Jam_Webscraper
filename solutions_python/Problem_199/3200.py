input = """3
---+-++- 3
+++++ 4
-+-+- 4
"""

output = """Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
"""


def solve(s, k):
    """
    0123
    .... len=4
    xxx  k=3
     xxx
    2: 0, 1
    ______________
    01234
    ..... len=5
    xx    k=2
     xx
      xx
       xx
    4: 0, 1, 2, 3
    """
    positions = len(s) - k + 1
    winning = list("+" * len(s))
    MAX = 9999

    def flip(ss, p):
        cc = list(ss)
        for i in xrange(p, p + k):
            cc[i] = "+" if cc[i] == "-" else "-"
        return cc

    def recur(p, ss, taken):
        if ss == winning:
            return taken
        if p >= positions:
            return MAX
        return min(recur(p + 1, ss, taken),
                   recur(p + 1, flip(ss, p), taken + 1))

    res = recur(0, list(s), 0)
    if res == MAX:
        return "IMPOSSIBLE"
    return res


def get_input(lines):
    out = []
    for i in xrange(1, len(lines)):
        if not lines[i]:
            continue
        s, k = lines[i].split(' ')
        res = solve(s, int(k))
        out.append("Case #%s: %s" % (i, res))
    return "\n".join(out)


# print get_input(input.split("\n"))
with open("A-small-attempt0.in") as file:
    print get_input(file.readlines())
