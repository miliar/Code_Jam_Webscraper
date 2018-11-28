from __future__ import division, print_function

import re, sys

def read_input(filename):
    tests = []
    with open(filename, 'rb') as f:
        count = int(f.readline())
        for index in xrange(count):
            (N, K) = [int(x) for x in f.readline().strip().split()]
            test = (index + 1, N, K, [f.readline().strip() for i in xrange(N)])
            tests.append(test)
    return tests

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            print("Case #%d: %s" % (r.index, r.winner),
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, winner):
        self.index = index
        self.winner = winner

    def __str__(self):
        return "Result #%d: %s" % (self.index, self.winner)

def compare_files(expected, got):
    with open(expected, 'rb') as i1:
        with open(got, 'rb') as i2:
            line = 1
            while True:
                try:
                    l1 = i1.next().rstrip()
                except StopIteration:
                    l1 = None
                try:
                    l2 = i2.next().rstrip()
                except StopIteration:
                    l2 = None
                    
                if l1 != l2:
                    print("At line %d, expected:" % line)
                    print(l1)
                    print("  but got:")
                    print(l2)
                    return False
                elif l1 is None:
                    break
                line += 1
    return True

def rotate_board(b):
    N = len(b)
    cols = []
    for i in xrange(N - 1, -1, -1):
        line = b[i]
        bottom_col = [c for c in line if c != '.']
        col = "." * (N - len(bottom_col)) + "".join(bottom_col)
        cols.append(col)
    return ["".join([cols[i][j] for i in xrange(N)])
            for j in xrange(N)]

dirs = [(1, 0), (1, -1), (0, -1), (-1, -1)]

def winner(b, c, K):
    N = len(b)
    for x in xrange(N):
        for y in xrange(N):
            if b[y][x] == c:
                for dx, dy in dirs:
                    for k in xrange(1, K):
                        nx = x + dx * k
                        ny = y + dy * k
                        if (0 <= nx < N) and (0 <= ny < N):
                            if b[ny][nx] != c:
                                break
                        else:
                            break
                    else:
                        #print("%d %d (%d,%d)" % (x, y, dx, dy))
                        return True
    return False
        
def solve_one(test):
    index, N, K, board = test
    rboard = rotate_board(board)
    b_wins = winner(rboard, "B", K)
    r_wins = winner(rboard, "R", K)
    result = (("Both" if r_wins else "Blue") if b_wins else
              ("Red" if r_wins else "Neither"))
    return Result(index, result)

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test) for test in tests]
    write_output(out_file, results)
    if check_file is not None:
        # File comparison
        if compare_files(check_file, out_file):
            print("Results match expected")

MY_FILES = ["sampleA", "A-small-attempt0", "A-small-attempt1"]
    
    
def main(filename=None):
    if filename is None:
        for f in MY_FILES:
            print("Solving %s" % f)
            solve(f + ".in", f + ".out", f + ".check", verbose=True)
            print("------------")
    else:
        real_filename = filename if not filename.endswith(".in") else filename[:-len(".in")]
        solve(real_filename + ".in", real_filename + ".out", verbose=False)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        main()
    else:
        main(sys.argv[1])
