
def read_cake(infile):
    rows, cols = (int(x) for x in infile.readline().strip().split())
    cake = []
    for r in range(0, rows):
        col = infile.readline().strip()
        assert len(col) == cols
        cake.append(list(col))
    return cake

def make_rects(cake):
    from_bottom_rows = []
    for rnum, row in enumerate(cake):
        fill_letter = None
        for cnum, letter in enumerate(row):
            if letter != '?':
                if fill_letter is None:
                    row[0:cnum] = [letter]*cnum
                fill_letter = letter
            elif fill_letter is not None:
                row[cnum] = fill_letter
        if fill_letter is None:
            if (rnum == 0) or ((len(from_bottom_rows) > 0)
                               and ((rnum - 1) == from_bottom_rows[-1])):
                from_bottom_rows.append(rnum)
            else:
                row[:] = cake[rnum - 1][:]
    from_bottom_rows.sort(reverse=True)
    for rnum in from_bottom_rows:
        cake[rnum][:] = cake[rnum + 1][:]
    return cake

import sys

def run_tests(infile):
    numtests = int(infile.readline())
    for test in range(0, numtests):
        cake = read_cake(infile)
        cake = make_rects(cake)
        print("Case #{}:".format(test + 1))
        print('\n'.join(''.join(row) for row in cake))

if __name__ == '__main__':
    run_tests(sys.stdin)
