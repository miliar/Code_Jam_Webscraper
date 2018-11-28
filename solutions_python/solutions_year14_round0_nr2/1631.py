import sys
import os.path

def get_line(iterator):
    row_no = int(next(iterator))

    for i in range(4):
        line = next(iterator)
        if i + 1 == row_no:
            ret = [int(x) for x in line.split()]

    return ret

def main(lines):
    it = iter(lines)

    n_cases = int(next(it))

    for i in range(n_cases):
        row_1 = get_line(it)
        row_2 = get_line(it)
        print "Case #%d:" % (i + 1),
        sol = solve(row_1, row_2)
        print sol
        if sol == "Impossible\n":
            # print args
            pass

def solve(row_1, row_2):
    possibilities = set(row_1) & set(row_2)
    if len(possibilities) > 1:
        return "Bad magician!"
    elif len(possibilities) == 1:
        return next(iter(possibilities))
    else:
        return "Volunteer cheated!"

if __name__=="__main__":
    filename = sys.argv[1]
    name, ext = os.path.splitext(filename)

    with open(filename) as instream:
        with open(name + ".out", "w") as outstream:
            origout = sys.stdout
            sys.stdout = outstream
            try:
                main(instream.readlines())
            finally:
                sys.stdout = origout
