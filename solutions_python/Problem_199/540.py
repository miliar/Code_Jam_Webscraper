import sys
import numpy as np

def solve_case(s, k):
    pan_ends = np.zeros(len(s), bool)
    initial_sides = [1 if c=='+' else -1 for c in s]
    current_pans = 0
    ans = 0
    for i,initial_side in enumerate(initial_sides):
        current_side = initial_side * ((-1)**current_pans)
        if current_side == -1:
            if i+k > len(initial_sides):
                return "IMPOSSIBLE"
            current_pans += 1
            ans += 1
            pan_ends[i+k-1] = True
        if pan_ends[i]:
            current_pans -= 1
    if current_pans > 0:
        print >> sys.stderr, "This shouldn't happen!"
        return "IMPOSSIBLE"
    return ans
        

def main():
    infile = sys.argv[1]
    inp = file(infile,"rb").read()
    lines = inp.splitlines()
    T = int(lines[0])
    for case_num, line in enumerate(lines[1:]):
        S,K = line.split(" ")
        K = int(K)
        ans = solve_case(S, K)
        print "Case #%d:"%(case_num+1), ans

if __name__ == "__main__":
    main()