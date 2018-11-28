def readFile(fname):
    f = open(fname)
    T = f.readline().strip()
    cases = []
    for line in f:
        cases.append(line.strip().split()[-1])
    return cases

def solve(cases):
    ans = []
    for i in range(len(cases)-1,-1,-1):
        if sum([int(case) for case in cases[0:i]]) < i:
            ans.append(i - sum([int(case) for case in cases[0:i]]))

    return max(ans) if len(ans) > 0 else 0

def test():
    for case in ["11111","09","110011","1"]:
        print "New Test: " + case
        print solve(case)

def main():
    fname = raw_input("Please input a filename: ")
    solve(readFile(fname))
