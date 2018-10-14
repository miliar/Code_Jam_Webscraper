name = "B-small-attempt0"
input = name + ".in"
output = name + ".out"

colors = ["R", "O", "Y", "G", "B", "V"]
primaries = ["R", "Y", "B"]
def is_primary(color):
    return color in primaries
def to_primary(color):
    if   color == "R":
        return (True, False, False)
    elif color == "O":
        return (True, True, False)
    elif color == "Y":
        return (False, True, False)
    elif color == "G":
        return (False, True, True)
    elif color == "B":
        return (False, False, True)
    elif color == "V":
        return (True, False, True)
def from_primary(p):
    for color in colors:
        if p == to_primary(color):
            return color
def complementary(color):
    return from_primary(tuple(map(lambda b: not b, to_primary(color))))
def are_compatible(c1, c2):
    p1 = to_primary(c1)
    p2 = to_primary(c2)
    for i in range(3):
        if p1[i] and p2[i]:
            return False
    return True
def compatibles(color):
    comp = []
    for c2 in colors:
        if are_compatible(color, c2):
            comp.append(c2)
    return comp

def solve(n, r, o, y, g, b, v):
    state = {"R":r, "O":o, "Y":y, "G":g, "B":b, "V":v}

    def get_unicorn(color=None):
        if color is None:
            for color in colors:
                if get_unicorn(color):
                    return color
            return None

        nb = state[color]
        if nb == 0:
            return False
        state[color] = nb - 1
        return True

    def next(color):
        compl = complementary(color)

        if get_unicorn(compl):
            return compl
        else:
            candidates = compatibles(color)
            candidates.sort(key=lambda c: state[c], reverse=True)  # Sort by decreasing count
            for c in candidates:
                if get_unicorn(c):
                    return c
            return None

    last = get_unicorn()
    order = last
    for _ in range(n-1):
        next_one = next(last)
        if next_one is None:
            return "IMPOSSIBLE"

        last = next_one
        order += next_one

    if are_compatible(order[0], order[-1]):
        return order
    return "IMPOSSIBLE"

line = -1
with open(input) as f:
    f_out = open(output, 'w')
    lines = f.readlines()

    def read_line():
        global line
        line += 1
        print(lines[line])
        return lines[line]

    t = int(read_line())

    for i in range(1, t+1):
        n, r, o, y, g, b, v = map(int, read_line().split())

        f_out.write("Case #%d: %s\n" % (i, solve(n, r, o, y, g, b, v)))