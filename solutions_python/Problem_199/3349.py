
def all_happy(cake):
    return all(c == "+" for c in cake)


def switch_chars(s):
    return s.replace("+", "x").replace("-", "+").replace("x", "-")


def do_flip(cake, K):
    index = cake.index("-")
    if index + K > len(cake):
        index = len(cake)-K
    return cake[:index] + switch_chars(cake[index: index+K]) + cake[index+K:]


def flip_it(cake, K):
    count = 0
    history = []
    while not all_happy(cake):
        count += 1
        # print "Will Flip: %d %s" % (count, cake)
        history.append(cake)
        cake = do_flip(cake, K)
        if cake in history:
            return "IMPOSSIBLE"
        # print ["all_happy(cake)", cake, all_happy(cake)]
    return count


outp = open("panacake-output", "w")
cache = {}
cases = []
solutions = []
with open("A-large.in") as f:
    skip = True
    case = 0
    for l in f:
        if skip:
            skip = False
        else:
            case += 1
            cake, K = l.split()
            y = flip_it(cake, int(K))
            print("Case #%d: %s" % (case, y))
            outp.write("Case #%d: %s\n" % (case, y))
