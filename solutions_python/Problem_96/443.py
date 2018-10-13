import sys, os

def best_score(total, surprising):
    # hard code low numbers to avoid dealing with negatives
    if total == 0: return 0
    if total == 1: return 1
        
    avg = total / 3
    rem = total % 3
    if not surprising:
        # as long as we have a remainder we can bump this up
        return avg + (1 if rem != 0 else 0)
    else:
        return avg + (2 if rem == 2 else 1)

def solve_line(line):
    vals = map(lambda x: int(x), line.strip().split(" "))
    n = vals[0]
    s = vals[1]
    p = vals[2]
    scores = vals[3:]
    assert n == len(scores)
    no_surprises, surprises = 0, 0
    for score in scores:
        if best_score(score, False) >= p:
            no_surprises += 1
        elif best_score(score, True) >= p:
            surprises += 1
    return no_surprises + min(surprises, s)
        
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
    solve("B-large.in")