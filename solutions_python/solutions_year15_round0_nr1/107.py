def solve(lineNo, n_by_s):
    num_sofar = 0
    ans = 0
    for shyness, num in enumerate(n_by_s):
        if shyness > num_sofar:
            lack = shyness - num_sofar
            ans += lack
            num_sofar += lack
        num_sofar += num
    print("Case #%d: %d" % (lineNo, ans))

fin = open('A-large.in')
lines = fin.readlines()[1:]
fin.close()

for lineNo, line in enumerate(lines):
    tokens = line.strip().split()
    smax = int(tokens[0])
    n_by_s = list(map(int, tokens[1]))
    solve(lineNo+1, n_by_s)
