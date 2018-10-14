def solve(d, n, hs):
    mx = 0
    for i in range(n):
        if mx < float(d-hs[i][0])/hs[i][1]:
            mx = float(d-hs[i][0])/hs[i][1]

    return float(d)/mx;

fin = open('A-large.in', 'r')
fout = open('a.out', 'w')

t = int(fin.readline())

for i in range(t):
    ins = fin.readline().split()
    d = int(ins[0])
    n = int(ins[1])
    hs = []
    for _ in range(n):
        inss = fin.readline().split()
        hs.append((int(inss[0]), int(inss[1])))
    fout.write("Case #" + str(i+1) + ": " + str(solve(d, n, hs)) + "\n")
