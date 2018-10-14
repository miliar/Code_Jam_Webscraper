'''
cat test_a.txt | python problem_a.py
cat A-small-attempt0.in | python problem_a.py >A-small-attempt0.out
cat A-large.in | python problem_a.py >A-large.out
'''

from sys import stdin

def solve(grid, r, c):
    r_count = [0] * r
    c_count = [0] * c
    r_min = [c-1] * r
    r_max = [0] * r
    c_min = [r-1] * c
    c_max = [0] * c
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] != '.':
                r_count[i] += 1
                r_min[i] = min(j, r_min[i])
                r_max[i] = max(j, r_max[i])
                c_count[j] += 1
                c_min[j] = min(i, c_min[j])
                c_max[j] = max(i, c_max[j])
    result = 0
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] == '.':
                continue
            if r_count[i] == 1 and c_count[j] == 1:
                return None
            if grid[i][j] == '<' and r_min[i] < j:
                continue
            if grid[i][j] == '>' and r_max[i] > j:
                continue
            if grid[i][j] == '^' and c_min[j] < i:
                continue
            if grid[i][j] == 'v' and c_max[j] > i:
                continue
            result += 1
    return result

def main():
    tt = int(stdin.readline().strip())
    for t in xrange(1, tt+1):
        (r, c) = (int(s) for s in stdin.readline().strip().split(' '))
        grid = list()
        for _ in xrange(r):
            line = stdin.readline().strip()
            grid.append(line)
        result = solve(grid, r, c)
        print "Case #{}: {}".format(t, "IMPOSSIBLE" if result is None else result)

main()
