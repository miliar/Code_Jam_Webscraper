from __future__ import division, print_function

import re, sys
import fractions

def read_input(filename):
    with open(filename, 'rb') as f:
        count = int(f.readline())
        tests = [(index + 1, [int(x) for x in f.readline().strip().split()][1:])
                 for index in xrange(count)]
    return tests

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            print("Case #%d: %d" % (r.index, r.count), # real result line
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, count):
        self.index = index
        self.count = count

    def __str__(self):
        return "Result #%d: %d" % (self.index, self.count)

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

def solve_one(test):
    (index, times) = test
    stimes = sorted(times)
    dgcd = None
    for i0 in xrange(len(stimes) - 1):
        t0 = stimes[i0]
        for i1 in xrange(i0 + 1, len(stimes)):
            t1 = stimes[i1]
            if dgcd is None:
                dgcd = t1 - t0
            else:
                dgcd = fractions.gcd(dgcd, t1 - t0)
    rem = stimes[0] % dgcd
    #print("dgcd=%d, rem=%d" % (dgcd, rem))
    return Result(index, 0 if rem == 0 else dgcd - rem)

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test) for test in tests]
    write_output(out_file, results)
    if check_file is not None:
        # File comparison
        if compare_files(check_file, out_file):
            print("Results match expected")

MY_FILES = ["sampleB"]
    
    
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
