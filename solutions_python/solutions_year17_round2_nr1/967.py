inp = 'A-large.in'
out = inp.split('.')[0] + '.out'

g = open(out, 'w')
with open(inp, 'r') as f:
    T = int(f.readline().strip())
    for i in range(1, T+1):
        line = f.readline().split()
        D, N = int(line[0]), int(line[1])
        slowest = 0
        for j in range(N):
            line = f.readline().split()
            k, s = int(line[0]), int(line[1])
            slowest = max((D-k) / s, slowest)
        const_speed = D / slowest
        print("Case #{0}: {1:.6f}".format(i, const_speed), file=g)
g.close()