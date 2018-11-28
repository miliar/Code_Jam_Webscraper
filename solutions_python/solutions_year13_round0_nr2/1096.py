import sys
inputfilename = sys.argv[1]

def solve(lst):
    solution = []
    for row in lst:
        solution.append([max(row)] * len(row))
    for col, i in (([row[i] for row in lst], i) for i in range(len(lst[0]) )):
        max_ideal = max(col)
        max_solution = max([row[i] for row in solution])
        if max_ideal > max_solution:
            continue
        # copy row
        for row in solution:
            if max_ideal < row[i]:
                row[i] = max_ideal
    return "YES" if solution == lst else "NO"

with open(inputfilename) as fp:
    N = int(fp.readline())
    for pr in range(N):
        rows, cols = map(int, fp.readline().split())
        problem = []
        for i in range(rows):
            problem.append(map(int, fp.readline().strip().split()))
        print "Case #%s: %s" %(pr+1, solve(problem))
        