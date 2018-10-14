def tidy(s):
    if len(s) < 2:
        return s
    last_tidy = tidy(s[1:])
    if int(s[0]) <= int(last_tidy[0]):
        return s[0:1] + last_tidy
    else:
        return str(int(s[0]) - 1) + "9" * (len(s) - 1)

def solve_one(s):
    return str(int(tidy(s)))

def solve(data, f):
    lines = data.split("\n")
    T = int(lines[0])
    ncase = 0
    for line in lines[1:(T + 1)]:
        ncase += 1
        ans = solve_one(line.strip())
        f.write("Case #%d: %s\n" % (ncase, ans))

def solve_files(infile, outfile):
    data = open(infile, "rt").read()
    with open(outfile, "wt") as f:
        solve(data, f)


    
