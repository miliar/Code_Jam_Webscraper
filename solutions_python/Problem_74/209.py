def calc_time(seq):
    robot2index = {"B": 0, "O": 1}
    pos = [1, 1]
    time = [0, 0]
    for item in zip(seq[::2], seq[1::2]):
        robot = robot2index[item[0]]
        button = int(item[1])
        
        time[robot] = max(time[robot] + abs(button - pos[robot]) + 1,
                   time[robot^1] + 1)

        pos[robot] = button
    return max(time)

def solve_A(infile, outfile):
    inputs = open(infile).readlines()[1:]
    R = []
    for i, inp in enumerate(inputs):
        res = calc_time(inp.split()[1:])
        R.append("Case #%d: %d" % (i + 1, res))
    
    open(outfile, "w").write("\n".join(R))
