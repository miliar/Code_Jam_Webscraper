# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def find_seed(t_list):
    seed = "?"
    for c in t_list:
        if c != "?":
            seed = c
            break
    return seed

def find_seed_row(grid):

    for row in grid:
        if row[0] != "?":
            return row
    #else return none

def solve(grid):
    #first pass, fill row
    for num_row, row in enumerate(grid):
        seed = find_seed(row)
        if seed == "?":
            continue
        for num_c, c in enumerate(row):
            if c == "?":
                #print num_row, num_c
                grid[num_row][num_c] = seed
            else:
                seed = c

    #second pass, fill col:
    #howto?
    seed_row = find_seed_row(grid)
    for num_row, row in enumerate(grid):
        if row[0] == "?":
            grid[num_row] = seed_row
        else:
            seed_row = row
    return grid

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #n = int(raw_input())
    sample =[]
    for line in xrange(n):
        line_string = raw_input()
        sample.append(list(line_string))
    result = solve(sample)
    #print "Case #{}: {} {}".format(i, n + m, n * m)
    print "Case #{}:".format(i)
    for row in result:
        print "".join(row)
    # check out .format's specification for more formatting options