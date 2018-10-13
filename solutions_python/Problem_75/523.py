from __future__ import division, print_function

import re, sys

def read_input(filename):
    with open(filename, 'rb') as f:
        count = int(f.readline())
        tests = []
        for index in xrange(count):
            tline = f.readline().strip().split()
            C = int(tline[0])
            comb = tline[1:C + 1]
            D = int(tline[C + 1])
            opp = tline[C + 2: C + D + 2]
            N = int(tline[C + D + 2])
            inv = tline[C + D + 3]
            tests.append((index + 1, comb, opp, inv))
    return tests

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            s = ""
            for c in r.res:
                if len(s) > 0:
                    s += ", "
                s += c
            print("Case #%d: [%s]" % (r.index, s), # real result line
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, res):
        self.index = index
        self.res = res

    def __str__(self):
        return "Result #%d: %s" % (self.index, self.res)

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

def opposites(q, opp):
    last = q[-1]
    for o in opp:
        if last in o:
            for other in q[0:-1]:
                if (other != last) and (other in o):
                    return True
    return False

def combination(e1, e2, comb):
    c1 = e1 + e2
    c2 = e2 + e1
    for c in comb:
        if c[:2] == c1 or c[:2] == c2:
            return c[2]
    return None

def solve_one(test, verbose=False):
    index = test[0]
    print("Solving case#%d" % index)
    q = []
    comb = test[1]
    opp = test[2]
    inv = test[3]
    if verbose:
        print("Combinations: %s" % comb)
        print("Opposites: %s" % opp)
        print("Invoking: %s" % inv)
    for elem in inv:
        q.append(elem)
        something_happened = True
        while something_happened:
            something_happened = False
            while len(q) >= 2:
                res = combination(q[-2], q[-1], comb)
                if res is not None:
                    q[-2:] = [res]
                    something_happened = True
                else:
                    break
                
            if len(q) > 0:
                if opposites(q, opp):
                    q = []
                    something_happened = True
    print("Result: %s" % q)
    return Result(index, q)

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test, verbose=verbose) for test in tests]
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
