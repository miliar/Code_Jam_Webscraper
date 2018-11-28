def get_grid(f):
    rows = [map(lambda x: int(x.strip()), f.readline().split()) for i in range(4)]
    return rows

with open("/Users/nish/Downloads/A-small-attempt0.in") as f:
    num_test_cases = int(f.readline())
    for t in range(num_test_cases):
        first_guess = int(f.readline())
        first_grid = get_grid(f)
        second_guess = int(f.readline())
        second_grid = get_grid(f)
        diff = set(first_grid[first_guess-1]) & set(second_grid[second_guess-1])
        if len(diff) == 1:
            print "Case #%d: %d" % (t+1, diff.pop())
        elif len(diff) == 0:
            print "Case #%d: Volunteer cheated!" % (t+1)
        else:
            print "Case #%d: Bad magician!" % (t+1)
