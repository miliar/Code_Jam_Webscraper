import os
import os.path

def check(i, notes):
    for n in notes:
        if i % n != 0 and n % i != 0:
            return False
    return True

def solve(lower, upper, notes):
    for i in range(lower, upper+1):
        if check(i, notes):
            return i
    return "NO"

def harmony(path):
    fin = open(path)
    out_path = os.path.splitext(path)[0] + ".sol"
    fout = open(out_path, "w")

    num_cases = int(fin.readline().strip())

    for i in range(num_cases):
        num, lower, upper = fin.readline().strip().split()
        num = int(num)
        lower = int(lower)
        upper = int(upper)
        notes = fin.readline().strip().split()
        notes = [int(n) for n in notes]
        sol = solve(lower, upper, notes)
        fout.write("Case #%i: %s\n" % (i+1, sol))

    fout.close()
    fin.close()
