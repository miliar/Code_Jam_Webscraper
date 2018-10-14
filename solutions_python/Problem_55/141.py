from __future__ import division, print_function

import re, sys

def read_input(filename):
    with open(filename, 'rb') as f:
        count = int(f.readline())
        tests = []
        for index in xrange(count):
            [R, k, N] = [int(x) for x in f.readline().strip().split()]
            groups = [int(x) for x in f.readline().strip().split()]
            tests.append((index + 1, R, k, N, groups))
    return tests

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            print("Case #%d: %d" % (r.index, r.money), # real result line
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, money):
        self.index = index
        self.money = money

    def __str__(self):
        return "Result #%d: %d" % (self.index, self.money)

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



def solve_one(test, verbose=False):
    (index, R, k, N, groups) = test
    acc_groups = [groups]
    for i in xrange(2, N + 1):
        pg = acc_groups[i - 2]
        gi = [pg[j] + groups[(j + i - 1) % N]
              for j in xrange(N)]
        acc_groups.append(gi)
    for j in xrange(N):
        for i in xrange(N):
            if acc_groups[j][i] > k:
                acc_groups[j][i] = None

    # Size of max accumulated groups fitting a ride
    sizes = [max(acc_groups[j][i] for j in xrange(N))
             for i in xrange(N)]
    # Next index
    next = []
    for i in xrange(N):
        maxi = sizes[i]
        for j in xrange(N):
            if acc_groups[j][i] == maxi:
                next.append((i + j + 1) % N)
                break

    total = 0
    pos = 0
    prev_round = [None for x in xrange(N)]
    prev_total = [0 for x in xrange(N)]
    for r in xrange(R):
        if prev_round[pos] is None:
            prev_round[pos] = r
            prev_total[pos] = total
            total += sizes[pos]
            pos = next[pos]
            
        else: # Cycle found
            break

    else:
        return Result(index, total)

    if verbose:
        print("r=%d, pos=%d, total=%d, prev_round=%d, prev_total=%d" %
              (r, pos, total, prev_round[pos], prev_total[pos]))
    remaining_rounds = R - r
    if verbose:
        print("rounds left: %d" % remaining_rounds)
    cycle_length = r - prev_round[pos]
    if verbose:
        print("cycle length: %d" % cycle_length)
    cycle_money = total - prev_total[pos]
    if verbose:
        print("cycle money: %d" % cycle_money)
    cycles_left = remaining_rounds // cycle_length
    if verbose:
        print("cycles left: %d" % cycles_left)
    total += cycles_left * cycle_money
    rounds_after = remaining_rounds - cycles_left * cycle_length
    if verbose:
        print("rounds after cycles: %d" % rounds_after)
    for r in xrange(rounds_after):
        total += sizes[pos]
        pos = next[pos]
    
    return Result(index, total)

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test) for test in tests]
    write_output(out_file, results)
    if check_file is not None:
        # File comparison
        if compare_files(check_file, out_file):
            print("Results match expected")

MY_FILES = ["sampleC"]
    
    
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
