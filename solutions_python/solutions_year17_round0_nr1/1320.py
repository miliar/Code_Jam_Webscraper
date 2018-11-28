def solve_one(state, k):
    count = 0
    i = 0
    state = [(x == "+") for x in state]
    while i + k <= len(state):
        if not state[i]:
            count += 1
            for j in range(i, i + k):
                state[j] = not state[j]
        i += 1
    return all(state), count

def solve(data, f):
    lines = data.split("\n")
    T = int(lines[0])
    ncase = 0
    for line in lines[1:(T + 1)]:
        ncase += 1
        state, k = line.split()
        k = int(k)
        success, count = solve_one(state, k)
        if success:
            f.write("Case #%d: %d\n" % (ncase, count))
        else:
            f.write("Case #%d: IMPOSSIBLE\n" % ncase)

def solve_files(infile, outfile):
    data = open(infile, "rt").read()
    with open(outfile, "wt") as f:
        solve(data, f)


    
