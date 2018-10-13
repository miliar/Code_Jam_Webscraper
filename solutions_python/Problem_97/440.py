import sys, os

def pairs_below(val, upper_bound):
    valstr = str(val)
    def shift(amt):
        # 3456, 1 -> 4563 
        # 3456, 3 -> 6345
        return int("".join(valstr[amt:] + valstr[:amt]))
    matches = []
    for i in range(1, len(valstr)):
        shifted = shift(i)
        if val < shifted <= upper_bound and len(str(shifted)) == len(valstr):
            matches.append(shifted)
    return len(set(matches))
        
def solve_line(line):
    lower, upper = map(lambda x: int(x), line.strip().split(" "))
    total = 0
    for i in range(lower, upper + 1):
        total += pairs_below(i, upper)
    return total

def solve(filename):
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(fname) as data:
        first = True
        case = 1
        for line in data:
            if first:
                games = int(line)
                first = False
            else:
                print "Case #%s: %s" % (case, solve_line(line))
                case += 1

if __name__ == "__main__":
    solve("C-large.in")