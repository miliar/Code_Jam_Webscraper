from __future__ import division, print_function

import re, sys

def read_input(filename):
    with open(filename, 'rb') as f:
        count = int(f.readline())
        cases = [(i + 1, [int(k) for k in f.readline().strip().split()])
                  for i in xrange(count)]
    return cases

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            print("Case #%d: %s" % (r.index, "ON" if r.on_off else "OFF"),
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, on_off):
        self.index = index
        self.on_off = on_off

    def __str__(self):
        return "Result #%d: %d" % (self.index, self.count)

def compare_files(f1, f2):
    with open(f1, 'rb') as i1:
        with open(f2, 'rb') as i2:
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

def one_snap(chain):
    res = [not chain[i] if i == 0 or chain[i - 1] else chain[i]
           for i in xrange(len(chain))]
    return res

def simple_run(N, K):
    chain = [False for n in xrange(N)]
    for k in xrange(K):
        chain = one_snap(chain)
    return chain[-1] and (N == 1 or chain[-2])
    

def quick_answer(N, K):
    mask = 2 ** N - 1
    return K & mask == mask

def solve_one(c):
    (index, [N, K]) = c
    return Result(index, quick_answer(N, K))

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test) for test in tests]
    write_output(out_file, results)
    if check_file is not None:
        # File comparison
        if compare_files(out_file, check_file):
            print("Results match expected")

MY_FILES = ["sampleA"]
    
    
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
